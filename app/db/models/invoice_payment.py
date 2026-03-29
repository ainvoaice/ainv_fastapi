from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class InvoicePayment(Base, BaseMixin):
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

    invoice = relationship("Invoice", back_populates="payments")
