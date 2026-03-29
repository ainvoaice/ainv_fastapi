from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable
from uuid import UUID, uuid4

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import (
    ZBeDB,
    Client,
    Fee,
    Invoice,
    InvoiceItem,
    InvoicePayment,
    Item,
    PaymentMethod,
    PlanDB,
    Tax,
    ZMeDB,
)
from app.db.seeds.data_invoicing import build_seed_payloads


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _apply_base_fields(row: dict, *, ten_id: UUID, biz_id: UUID | None, owner_id: UUID, created_by: UUID | None) -> dict:
    row = dict(row)
    row.update(
        {
            "ten_id": ten_id,
            "biz_id": biz_id,
            "owner_id": owner_id,
            "created_by": created_by or owner_id,
        }
    )
    return row


async def _ensure_plans(session: AsyncSession, *, ten_id: UUID, owner_id: UUID) -> dict[str, UUID]:
    payloads = build_seed_payloads()
    plans = payloads["plans"]
    code_to_id: dict[str, UUID] = {}

    for plan in plans:
        existing = await session.scalar(select(PlanDB).where(PlanDB.plan_code == plan["plan_code"]))
        if existing:
            code_to_id[plan["plan_code"]] = existing.id
            continue

        row = _apply_base_fields(plan, ten_id=ten_id, biz_id=None, owner_id=owner_id, created_by=owner_id)
        plan_obj = PlanDB(**row)
        session.add(plan_obj)
        await session.flush()
        code_to_id[plan["plan_code"]] = plan_obj.id

    return code_to_id


async def ensure_invoicing_seeds_for_user(
    session: AsyncSession,
    *,
    ten_id: UUID,
    owner_id: UUID,
    auth_uid: UUID | None = None,
    email: str | None = None,
) -> UUID:
    """
    Ensures a new user has a full demo dataset:
    - user profile (zme)
    - business entity
    - items, clients, payment methods, taxes, fees
    - 3 demo invoices with items + payments
    """
    now = _utcnow()

    # User profile (zme)
    user = await session.scalar(select(ZMeDB).where(ZMeDB.id == owner_id))
    if not user:
        payloads = build_seed_payloads(now)
        user_row = payloads["user_profile"]
        user_row["u_referral_code"] = (str(auth_uid).replace("-", "")[:6] if auth_uid else None)
        user_row = _apply_base_fields(user_row, ten_id=ten_id, biz_id=None, owner_id=owner_id, created_by=owner_id)
        user = ZMeDB(id=owner_id, auth_uid=auth_uid, **user_row)
        session.add(user)

    # Plans (global-ish)
    plan_ids = await _ensure_plans(session, ten_id=ten_id, owner_id=owner_id)

    # Business entity
    biz = await session.scalar(
        select(ZBeDB).where(ZBeDB.user_id == owner_id)
    )
    if not biz:
        payloads = build_seed_payloads(now)
        biz_row = payloads["business_entity"]
        biz_id = uuid4()
        plan_id = plan_ids.get("plan25_1")
        biz_row = _apply_base_fields(biz_row, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        biz = ZBeDB(
            id=biz_id,
            user_id=owner_id,
            be_plan_id=plan_id,
            **biz_row,
        )
        session.add(biz)
    else:
        biz_id = biz.id

    # If invoices already exist, assume the demo data is in place
    existing_invoice = await session.scalar(
        select(Invoice.id).where(Invoice.biz_id == biz_id)
    )
    if existing_invoice:
        return biz_id

    payloads = build_seed_payloads(now)

    # Fees
    fee_rows = []
    for fee in payloads["fees"]:
        row = _apply_base_fields(fee, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        fee_rows.append(Fee(user_id=owner_id, **row))
    session.add_all(fee_rows)

    # Payment methods
    pm_rows = []
    pm_code_to_id: dict[str, UUID] = {}
    for pm in payloads["payment_methods"]:
        row = _apply_base_fields(pm, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        pm_obj = PaymentMethod(user_id=owner_id, **row)
        session.add(pm_obj)
        await session.flush()
        pm_code_to_id[pm["pm_code"]] = pm_obj.id
        pm_rows.append(pm_obj)

    # Taxes
    tax_rows = []
    for tax in payloads["taxes"]:
        row = _apply_base_fields(tax, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        tax_rows.append(Tax(user_id=owner_id, **row))
    session.add_all(tax_rows)

    # Clients
    client_rows = []
    client_code_to_id: dict[str, UUID] = {}
    for client in payloads["clients"]:
        row = _apply_base_fields(client, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        client_obj = Client(user_id=owner_id, **row)
        session.add(client_obj)
        await session.flush()
        client_code_to_id[client["client_code"]] = client_obj.id
        client_rows.append(client_obj)

    # Items
    item_rows = []
    item_code_to_id: dict[str, UUID] = {}
    for item in payloads["items"]:
        row = _apply_base_fields(item, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        if "item_unit" in row and "item_unit_of_measure" not in row:
            row["item_unit_of_measure"] = row["item_unit"]
        item_obj = Item(user_id=owner_id, **row)
        session.add(item_obj)
        await session.flush()
        item_code_to_id[item["item_code"]] = item_obj.id
        item_rows.append(item_obj)

    # Invoices + invoice items/payments
    for inv in payloads["invoices"]:
        inv_row = dict(inv)
        inv_row.pop("items", None)
        inv_row.pop("payments", None)
        inv_row = _apply_base_fields(inv_row, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
        client_code = inv.get("client_code")
        inv_row["client_id"] = client_code_to_id.get(client_code)
        inv_row["inv_tnc"] = inv_row.get("inv_terms_conditions")
        invoice = Invoice(user_id=owner_id, **inv_row)
        session.add(invoice)
        await session.flush()

        for inv_item in inv.get("items", []):
            item_row = _apply_base_fields(inv_item, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
            item_code = inv_item.get("item_code")
            item_row["item_id"] = item_code_to_id.get(item_code)
            if "item_unit" in item_row and "item_unit_of_measure" not in item_row:
                item_row["item_unit_of_measure"] = item_row["item_unit"]
            invoice_item = InvoiceItem(inv_id=invoice.id, **item_row)
            session.add(invoice_item)

        for payment in inv.get("payments", []):
            pay_row = _apply_base_fields(payment, ten_id=ten_id, biz_id=biz_id, owner_id=owner_id, created_by=owner_id)
            pm_code = payment.get("pm_code")
            pay_row["pm_id"] = pm_code_to_id.get(pm_code)
            invoice_payment = InvoicePayment(inv_id=invoice.id, **pay_row)
            session.add(invoice_payment)

    return biz_id
