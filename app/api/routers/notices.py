# crud.py
# Imports
from fastapi import HTTPException, APIRouter, Depends
from typing import Optional, List
from app.database.db_raw import *

# Defines the Router
notices_router = APIRouter(
prefix="/notices",
tags=["Notices"])

# Get Driver's Notice Details by ID
@notices_router.get("/{driver_id}")
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