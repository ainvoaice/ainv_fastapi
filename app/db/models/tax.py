from uuid import UUID

from sqlalchemy import ForeignKey, Integer, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class Tax(Base, BaseMixin):
    __tablename__ = "taxes"

    user_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("zme.id"), index=True)
    be_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("business_entities.id"), index=True)

    tax_name: Mapped[str | None] = mapped_column(String(128))
    tax_rate: Mapped[float | None] = mapped_column(Numeric(8, 4))
    tax_type: Mapped[str | None] = mapped_column(String(64))
    tax_note: Mapped[str | None] = mapped_column(String(1024))

    business = relationship("BusinessEntity", back_populates="taxes")
