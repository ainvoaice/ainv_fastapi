from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.m_invoice import InvoiceDB
from app.schemas.sch_invoice import InvoiceCreate


async def list_all_invoices(db: AsyncSession):
    result = await db.execute(
        select(InvoiceDB).where(InvoiceDB.is_deleted != True)
    )
    return list(result.scalars().all())


async def create_invoice(data: InvoiceCreate, db: AsyncSession):
    payload = data.model_dump(exclude_unset=True)
    invoice = InvoiceDB(**payload)
    db.add(invoice)
    await db.flush()
    await db.refresh(invoice)
    return invoice
