from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

from app.db.db_async import get_session
from app.schemas.sch_payroll_entry import (
    PayrollEntryCreate,PayrollEntryResponse,PayrollPeriodCreate,
    PayrollPeriodResponse,PayrollScheduleCreate,PayrollScheduleResponse,
)
from app.service.ser5_payroll_schedule import (
    create_entry,list_entries_by_period,finalize_entry,
    create_period,get_period,list_periods,finalize_period,
    create_schedule,get_schedule,list_schedules,edit_schedule,deactivate_schedule,
)

payrollRou = APIRouter()

# ---- PAYROLL SCHEDULE ENDPOINTS ----

@payrollRou.post("/schedule",
    response_model=PayrollScheduleResponse,
    summary="Create a new payroll schedule",
    responses={
        201: {"description": "Payroll schedule created successfully"},
        400: {"description": "Invalid input data"},
    }
)
async def create_payroll_schedule(
    data: PayrollScheduleCreate,
    db: AsyncSession = Depends(get_session),
):
    """
    Create a new payroll schedule with frequency, anchor date, and effective dates.
    
    Supported frequencies: weekly, biweekly, monthly
    """
    return await create_schedule(data, db)


@payrollRou.get("/schedule/{schedule_id}",
    response_model=PayrollScheduleResponse,
    summary="Get a payroll schedule",
)
async def get_payroll_schedule(
    schedule_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Retrieve a specific payroll schedule by ID.
    """
    return await get_schedule(schedule_id, db)


@payrollRou.get("/schedules",
    response_model=List[PayrollScheduleResponse],
    summary="List all payroll schedules",
)
async def list_payroll_schedules(
    skip: int = Query(0, ge=0, description="Number of schedules to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum schedules to return"),
    db: AsyncSession = Depends(get_session),
):
    """
    Retrieve all payroll schedules with pagination.
    """
    return await list_schedules(db, skip=skip, limit=limit)


@payrollRou.put("/schedule/{schedule_id}",
    response_model=PayrollScheduleResponse,
    summary="Update a payroll schedule",
    responses={
        200: {"description": "Schedule updated successfully"},
        404: {"description": "Payroll schedule not found"},
        400: {"description": "Invalid input data"},
    }
)
async def update_payroll_schedule(
    schedule_id: UUID,
    data: PayrollScheduleCreate,
    db: AsyncSession = Depends(get_session),
):
    """
    Update an existing payroll schedule.
    """
    return await edit_schedule(schedule_id, data, db)


@payrollRou.patch("/schedule/{schedule_id}/deactivate",
    response_model=PayrollScheduleResponse,
    summary="Deactivate a payroll schedule",
    responses={
        200: {"description": "Schedule deactivated successfully"},
        404: {"description": "Payroll schedule not found"},
    }
)
async def deactivate_payroll_schedule(
    schedule_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Mark a payroll schedule as inactive. It will no longer be used for new periods.
    """
    return await deactivate_schedule(schedule_id, db)




@payrollRou.patch(
    "/entry/{entry_id}/finalize",
    response_model=PayrollEntryResponse,
    summary="Finalize a payroll entry",
    responses={
        200: {"description": "Entry finalized successfully"},
        404: {"description": "Payroll entry not found"},
    }
)
async def complete_entry(
    entry_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Mark a payroll entry as completed/finalized.
    """
    return await finalize_entry(entry_id, db)