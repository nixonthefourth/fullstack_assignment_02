# crud.py
# Imports
from fastapi import HTTPException, APIRouter, Depends
from typing import Optional, List
from db_raw import *
from models import *

# Defines the Router
router = APIRouter(
prefix="/crud",
tags=["crud"])

# Get Driver's Details by ID
@router.get("/driver/{driver_id: int}")
async def get_driver_details(driver_id: int):
    # Perform the Operation
    row = fetch_driver_details(driver_id)

    # Validation
    if row is None:
        raise HTTPException(status_code=404, detail="Driver ID Not Found")
    
    # Driver Details
    driver = {
        "driver_id": row[0],
        "licence_number": row[2],
        "state_issue": row[3],
        "last_name": row[4],
        "first_name": row[5],
        "dob": row[6],
        "height_inches": row[7],
        "weight_pounds": row[8],
        "eyes_colour": row[9]
    }

    # Return the Results
    return driver

# Get Driver's Notice Details by ID
@router.get("/notices/{driver_id: int}")
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

# Get All Driver's Details
@router.get("/drivers")
async def get_all_drivers():
    # Perform the Operation
    row = fetch_all_drivers()

    # Validation
    if row is None:
        raise HTTPException(status_code=404, detail="Driver ID Not Found")
    
    # All Drivers
    drivers = {
        "driver_id": row[0],
        "state_issue": row[1],
        "last_name": row[2],
        "first_name": row[3]
    }

    # Return
    return drivers