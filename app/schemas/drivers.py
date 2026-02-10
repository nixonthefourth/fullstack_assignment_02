# app/schemas/drivers.py

from pydantic import BaseModel
from datetime import date

# Base Model for Driver
# Primarily Used in GET
class DriverBase(BaseModel):
    driver_id: int
    licence_number: str
    state_issue: str
    last_name: str
    first_name: str
    dob: date
    height_inches: int
    weight_pounds: int
    eyes_colour: str
