from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .m_base import Base, BaseMixin


class PlanDB(Base, BaseMixin):
    __tablename__ = "plans"

    plan_code: Mapped[str | None] = mapped_column(String(64))
    plan_name: Mapped[str | None] = mapped_column(String(128))
    plan_price: Mapped[str | None] = mapped_column(String(64))
    plan_features: Mapped[list | None] = mapped_column(JSONB)
