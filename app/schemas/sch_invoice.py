from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class InvoiceBase(BaseModel):
    inv_code: str | None = None
    inv_number: str | None = None
    inv_issue_date: datetime | None = None
    inv_due_date: datetime | None = None

    inv_title: str | None = None
    inv_template_id: str | None = None

    client_id: UUID | None = None
    client_number: str | None = None
    client_company_name: str | None = None
    client_contact_name: str | None = None
    client_contact_title: str | None = None
    client_address: str | None = None
    client_email: str | None = None
    client_secondphone: str | None = None
    client_mainphone: str | None = None
    client_fax: str | None = None
    client_website: str | None = None
    client_business_number: str | None = None
    client_currency: str | None = None
    client_tax_id: str | None = None
    client_payment_term: int | None = None
    client_payment_method: str | None = None
    client_terms_conditions: str | None = None
    client_note: str | None = None

    inv_payment_term: int | None = None
    inv_payment_requirement: str | None = None
    inv_reference: str | None = None
    inv_currency: str | None = None

    inv_subtotal: Decimal | None = None
    inv_discount: Decimal | None = None
    inv_tax_label: str | None = None
    inv_tax_rate: Decimal | None = None
    inv_tax_amount: Decimal | None = None

    inv_shipping: Decimal | None = None
    inv_handling: Decimal | None = None
    inv_deposit: Decimal | None = None
    inv_adjustment: Decimal | None = None
    inv_other_charges_label: str | None = None
    inv_other_charges_amount: Decimal | None = None
    inv_total: Decimal | None = None

    inv_paid_total: Decimal | None = None
    inv_balance_due: Decimal | None = None
    inv_payment_status: str | None = None

    inv_tnc: str | None = None
    inv_notes: str | None = None

    inv_flag_word: str | None = None
    inv_flag_emoji: str | None = None
    inv_pdf_template: str | None = None
    inv_terms_conditions: str | None = None


class InvoiceCreate(InvoiceBase):
    locale: str | None = None
    ten_id: UUID | None = None
    biz_id: UUID | None = None
    zme_id: UUID | None = None
    owner_id: UUID | None = None
    created_by: UUID | None = None

    b_int: int | None = None
    b_str: str | None = None
    b_decimal: Decimal | None = None
    b_date: datetime | None = None
    b_bool: bool | None = None
    b_json: Dict[str, Any] | None = None

    is_deleted: bool | None = None
    is_flag: bool | None = None

    status: str | None = None
    type: str | None = None
    description: str | None = None


class InvoiceResponse(InvoiceCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
