# crud.py
# Imports
from fastapi import HTTPException, APIRouter, Depends
from typing import Optional, List
from app.database.db_raw import *
from app.schemas.drivers import *

# Defines the Router
drivers_router = APIRouter(
prefix="/drivers",
tags=["Drivers"])

# Get Driver's Details by ID
@drivers_router.get("/{driver_id}", response_model=DriverBase)
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

# Get All Driver's Details
@drivers_router.get("/")
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