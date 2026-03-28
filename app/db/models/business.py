from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class BusinessEntity(Base, BaseMixin):
    __tablename__ = "business_entities"

    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("zme.id"), index=True)

    be_logo: Mapped[str | None] = mapped_column(String(512))
    be_name: Mapped[str | None] = mapped_column(String(256))
    be_contact: Mapped[str | None] = mapped_column(String(128))
    be_contact_title: Mapped[str | None] = mapped_column(String(128))
    be_address: Mapped[str | None] = mapped_column(String(512))
    be_email: Mapped[str | None] = mapped_column(String(128))
    be_phone: Mapped[str | None] = mapped_column(String(64))
    be_website: Mapped[str | None] = mapped_column(String(256))
    be_type: Mapped[str | None] = mapped_column(String(64))

    be_biz_number: Mapped[str | None] = mapped_column(String(128))
    be_tax_id: Mapped[str | None] = mapped_column(String(128))
    be_bank_info: Mapped[str | None] = mapped_column(String(1024))
    be_payment_term: Mapped[int | None] = mapped_column(Integer)

    be_currency: Mapped[str | None] = mapped_column(String(16))
    be_inv_template_id: Mapped[str | None] = mapped_column(String(32))
    be_description: Mapped[str | None] = mapped_column(String(1024))
    be_note: Mapped[str | None] = mapped_column(String(1024))

    be_timezone: Mapped[str | None] = mapped_column(String(64))
    be_date_format: Mapped[str | None] = mapped_column(String(32))
    be_inv_prefix: Mapped[str | None] = mapped_column(String(32))
    be_inv_integer: Mapped[int | None] = mapped_column(Integer)
    be_inv_integer_max: Mapped[int | None] = mapped_column(Integer)

    be_show_paid_stamp: Mapped[bool | None] = mapped_column(Boolean, default=True)

    be_plan_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("plans.id"), nullable=True)
    be_plan_name: Mapped[str | None] = mapped_column(String(128))
    be_plan251_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan252_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan253_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan254_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan255_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan256_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan257_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan258_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    be_plan259_expired: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    user = relationship("ZMeDB", back_populates="businesses")
    clients = relationship("Client", back_populates="business", cascade="all, delete-orphan")
    items = relationship("Item", back_populates="business", cascade="all, delete-orphan")
    invoices = relationship("Invoice", back_populates="business", cascade="all, delete-orphan")
    payment_methods = relationship("PaymentMethod", back_populates="business", cascade="all, delete-orphan")
    taxes = relationship("Tax", back_populates="business", cascade="all, delete-orphan")
    fees = relationship("Fee", back_populates="business", cascade="all, delete-orphan")
