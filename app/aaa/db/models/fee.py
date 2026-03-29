from uuid import UUID

from sqlalchemy import ForeignKey, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class Fee(Base, BaseMixin):
    __tablename__ = "fees"

    user_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("zme.id"), index=True)
    be_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("business_entities.id"), index=True)

    fee_code: Mapped[str | None] = mapped_column(String(64), index=True)
    fee_name: Mapped[str | None] = mapped_column(String(128))
    fee_amount: Mapped[float | None] = mapped_column(Numeric(12, 2))
    fee_note: Mapped[str | None] = mapped_column(String(1024))

    business = relationship("BusinessEntity", back_populates="fees")
