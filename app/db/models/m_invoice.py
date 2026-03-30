from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .m_base import Base, BaseMixin


class InvoiceDB(Base, BaseMixin):
    __tablename__ = "invoices"

    inv_code: Mapped[str | None] = mapped_column(String(64), index=True)
    inv_number: Mapped[str | None] = mapped_column(String(64))
    inv_issue_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    inv_due_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    inv_title: Mapped[str | None] = mapped_column(String(256))
    inv_template_id: Mapped[str | None] = mapped_column(String(32))

    client_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("clients.id"), index=True)
    client_number: Mapped[str | None] = mapped_column(String(64))
    client_company_name: Mapped[str | None] = mapped_column(String(256))
    client_contact_name: Mapped[str | None] = mapped_column(String(128))
    client_contact_title: Mapped[str | None] = mapped_column(String(128))
    client_address: Mapped[str | None] = mapped_column(String(512))
    client_email: Mapped[str | None] = mapped_column(String(128))
    client_secondphone: Mapped[str | None] = mapped_column(String(64))
    client_mainphone: Mapped[str | None] = mapped_column(String(64))
    client_fax: Mapped[str | None] = mapped_column(String(64))
    client_website: Mapped[str | None] = mapped_column(String(256))
    client_business_number: Mapped[str | None] = mapped_column(String(128))
    client_currency: Mapped[str | None] = mapped_column(String(16))
    client_tax_id: Mapped[str | None] = mapped_column(String(128))
    client_payment_term: Mapped[int | None] = mapped_column(Integer)
    client_payment_method: Mapped[str | None] = mapped_column(String(64))
    client_terms_conditions: Mapped[str | None] = mapped_column(String(1024))
    client_note: Mapped[str | None] = mapped_column(String(1024))

    inv_payment_term: Mapped[int | None] = mapped_column(Integer)
    inv_payment_requirement: Mapped[str | None] = mapped_column(String(256))
    inv_reference: Mapped[str | None] = mapped_column(String(256))
    inv_currency: Mapped[str | None] = mapped_column(String(16))

    inv_subtotal: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_discount: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_tax_label: Mapped[str | None] = mapped_column(String(64))
    inv_tax_rate: Mapped[float | None] = mapped_column(Numeric(8, 4))
    inv_tax_amount: Mapped[float | None] = mapped_column(Numeric(12, 2))

    inv_shipping: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_handling: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_deposit: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_adjustment: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_other_charges_label: Mapped[str | None] = mapped_column(String(128))
    inv_other_charges_amount: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_total: Mapped[float | None] = mapped_column(Numeric(12, 2))

    inv_paid_total: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_balance_due: Mapped[float | None] = mapped_column(Numeric(12, 2))
    inv_payment_status: Mapped[str | None] = mapped_column(String(32))

    inv_tnc: Mapped[str | None] = mapped_column(String(1024))
    inv_notes: Mapped[str | None] = mapped_column(String(1024))

    inv_flag_word: Mapped[str | None] = mapped_column(String(64))
    inv_flag_emoji: Mapped[str | None] = mapped_column(String(16))
    inv_pdf_template: Mapped[str | None] = mapped_column(String(64))
    inv_terms_conditions: Mapped[str | None] = mapped_column(String(1024))



class InvoicePaymentDB(Base, BaseMixin):
    __tablename__ = "invoice_payments"

    inv_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("invoices.id"), index=True)

    pm_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("payment_methods.id"), nullable=True)
    pm_code: Mapped[str | None] = mapped_column(String(64), index=True)
    pm_name: Mapped[str | None] = mapped_column(String(128))
    pm_note: Mapped[str | None] = mapped_column(String(1024))

    pay_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    pay_amount: Mapped[float | None] = mapped_column(Numeric(12, 2))
    pay_reference: Mapped[str | None] = mapped_column(String(256))
    pay_note: Mapped[str | None] = mapped_column(String(1024))



class InvoiceItemDB(Base, BaseMixin):
    __tablename__ = "invoice_items"

    inv_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("invoices.id"), index=True)

    item_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("items.id"), nullable=True)
    item_code: Mapped[str | None] = mapped_column(String(64), index=True)
    item_number: Mapped[str | None] = mapped_column(String(64))
    item_name: Mapped[str | None] = mapped_column(String(256))
    item_rate: Mapped[float | None] = mapped_column(Numeric(12, 2))
    item_unit_of_measure: Mapped[str | None] = mapped_column(String(64))
    item_unit: Mapped[str | None] = mapped_column(String(64))
    item_sku: Mapped[str | None] = mapped_column(String(128))
    item_description: Mapped[str | None] = mapped_column(String(1024))

    item_quantity: Mapped[int | None] = mapped_column(Integer)
    item_note: Mapped[str | None] = mapped_column(String(1024))
    item_amount: Mapped[float | None] = mapped_column(Numeric(12, 2))

