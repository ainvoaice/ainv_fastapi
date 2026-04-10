from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .m_base import Base, BaseMixin


class ClientDB(Base, BaseMixin):
    __tablename__ = "clients"

    client_code: Mapped[str | None] = mapped_column(String(64), index=True)
    client_number: Mapped[str | None] = mapped_column(String(64))
    client_business_number: Mapped[str | None] = mapped_column(String(128))

    client_company_name: Mapped[str | None] = mapped_column(String(256))
    client_contact_name: Mapped[str | None] = mapped_column(String(128))
    client_contact_title: Mapped[str | None] = mapped_column(String(128))
    client_address: Mapped[str | None] = mapped_column(String(512))
    client_email: Mapped[str | None] = mapped_column(String(128))
    client_mainphone: Mapped[str | None] = mapped_column(String(64))
    client_secondphone: Mapped[str | None] = mapped_column(String(64))
    client_fax: Mapped[str | None] = mapped_column(String(64))
    client_website: Mapped[str | None] = mapped_column(String(256))

    client_currency: Mapped[str | None] = mapped_column(String(16))
    client_tax_id: Mapped[str | None] = mapped_column(String(128))
    client_payment_term: Mapped[int | None] = mapped_column(Integer)
    client_payment_method: Mapped[str | None] = mapped_column(String(64))

    client_template_id: Mapped[str | None] = mapped_column(String(32))
    client_terms_conditions: Mapped[str | None] = mapped_column(String(1024))
    client_note: Mapped[str | None] = mapped_column(String(1024))
    client_status: Mapped[str | None] = mapped_column(String(64))
