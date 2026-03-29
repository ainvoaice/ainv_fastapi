from uuid import UUID

from sqlalchemy import ForeignKey, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .m_base import Base, BaseMixin


class FeeDB(Base, BaseMixin):
    __tablename__ = "fees"
    fee_code: Mapped[str | None] = mapped_column(String(64), index=True)
    fee_name: Mapped[str | None] = mapped_column(String(128))
    fee_amount: Mapped[float | None] = mapped_column(Numeric(12, 2))
    fee_note: Mapped[str | None] = mapped_column(String(1024))


class TaxDB(Base, BaseMixin):
    __tablename__ = "taxes"
    tax_code: Mapped[str | None] = mapped_column(String(64), index=True)
    tax_name: Mapped[str | None] = mapped_column(String(128))
    tax_rate: Mapped[float | None] = mapped_column(Numeric(8, 4))
    tax_type: Mapped[str | None] = mapped_column(String(64))
    tax_note: Mapped[str | None] = mapped_column(String(1024))


class PaymentMethodDB(Base, BaseMixin):
    __tablename__ = "payment_methods"
    pm_code: Mapped[str | None] = mapped_column(String(64), index=True)
    pm_name: Mapped[str | None] = mapped_column(String(128))
    pm_note: Mapped[str | None] = mapped_column(String(1024))
