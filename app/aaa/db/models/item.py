from uuid import UUID

from sqlalchemy import ForeignKey, Integer, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class Item(Base, BaseMixin):
    __tablename__ = "items"

    user_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("zme.id"), index=True)
    be_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("business_entities.id"), index=True)

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

    business = relationship("BusinessEntity", back_populates="items")
