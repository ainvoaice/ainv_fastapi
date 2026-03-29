from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class Referral(Base, BaseMixin):
    __tablename__ = "referrals"

    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("zme.id"), index=True)

    ref_uid: Mapped[UUID | None] = mapped_column(Uuid)
    ref_email: Mapped[str | None] = mapped_column(String(128))
    ref_created_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ref_reward_term: Mapped[str | None] = mapped_column(String(128))

    user = relationship("ZMeDB", back_populates="referrals")
