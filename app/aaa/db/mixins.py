from datetime import datetime
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class TimestampMixin:
    created_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
    )


class StatusFlagsMixin:
    status: Mapped[str | None] = mapped_column(String(64), default="5 stars")
    is_active: Mapped[int | None] = mapped_column(Integer, default=1)
    is_locked: Mapped[int | None] = mapped_column(Integer, default=0)
    is_deleted: Mapped[int | None] = mapped_column(Integer, default=0)
