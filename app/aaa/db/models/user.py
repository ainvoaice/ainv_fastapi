from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, BaseMixin


class ZMeDB(Base, BaseMixin):
    __tablename__ = "zme"

    auth_uid: Mapped[UUID | None] = mapped_column(Uuid, unique=True, index=True, nullable=True)

    u_type: Mapped[str | None] = mapped_column(String(64))
    u_logo: Mapped[str | None] = mapped_column(String(512))
    u_reward_balance: Mapped[int | None] = mapped_column(Integer)
    u_locale: Mapped[str | None] = mapped_column(String(32))
    u_referral_code: Mapped[str | None] = mapped_column(String(64))
    u_referred_by: Mapped[str | None] = mapped_column(String(128))

    plan_type: Mapped[str | None] = mapped_column(String(64))
    plan_start: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    plan_expires: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    plan_is_active: Mapped[bool | None] = mapped_column(Boolean)

    referrals = relationship("Referral", back_populates="user", cascade="all, delete-orphan")
    businesses = relationship("BusinessEntity", back_populates="user", cascade="all, delete-orphan")
