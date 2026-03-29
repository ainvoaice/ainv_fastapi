from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class PaymentMethod(Base, BaseMixin):
    __tablename__ = "payment_methods"

    user_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("zme.id"), index=True)
    be_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("business_entities.id"), index=True)

    pm_code: Mapped[str | None] = mapped_column(String(64), index=True)
    pm_name: Mapped[str | None] = mapped_column(String(128))
    pm_note: Mapped[str | None] = mapped_column(String(1024))

    business = relationship("BusinessEntity", back_populates="payment_methods")
