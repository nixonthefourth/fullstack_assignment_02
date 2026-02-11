# app/api/routers/notices.py
# Imports
from fastapi import HTTPException, APIRouter, Depends
from typing import Optional, List
from app.database.db_raw import *
from app.schemas.notices import *

# Defines the Router
notices_router = APIRouter(
prefix="/notices",
tags=["Notices"])

# Get Driver's Notice Details by ID
@notices_router.get("/{driver_id}", response_model=NoticeBase)
async def get_driver_notice(driver_id: int):
    # Perform the Operation
    row = fetch_driver_notices(driver_id)

    # Validation
    if row is None:
        raise HTTPException(status_code=404, detail="Driver ID Not Found")
    
    # Notice Details
    notice = {
        "notice_id": row[0],
        "violation_date_time": row[3],
        "detachment": row[4],
        "violation_severity": row[5],
        "notice_status": row[6],
        "notification_sent": row[7],
        "entry_date": row[8],
        "expiry_date": row[9],
        "violation_description": row[10]
    }

    # Return the Results
    return notice

# Create New Notice
@notices_router.post("/", response_model=NoticeBase)
async def insert_new_notice(notice: NoticeCreate):

    notice_id = create_notice(notice, notice.violation_zip, notice.violation_address)

    if notice_id is None:
        raise HTTPException(
            status_code=400,
            detail="Car does not exist. Cannot issue notice."
        )

    return {
        "notice_id": notice.notice_id,
        "violation_date_time": notice.violation_date_time,
        "detachment": notice.detachment,
        "violation_severity": notice.violation_severity,
        "notice_status": notice.notice_status,
        "notification_sent": notice.notification_sent,
        "entry_date": notice.entry_date,
        "expiry_date": notice.expiry_date,
        "violation_description": notice.violation_description
    }

"""DELETE"""

# Delete Notice by ID
@notices_router.delete("/{notice_id}")
async def remove_notice(notice_id: str):

    deleted = delete_notice(notice_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Notice not found"
        )

    return {"message": f"Notice {notice_id} deleted successfully"}
