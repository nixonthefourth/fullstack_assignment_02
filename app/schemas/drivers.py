# app/schemas/drivers.py
from pydantic import BaseModel
from datetime import date

# Base Model
class DriverBase(BaseModel):
    licence_number: str
    state_issue: str
    last_name: str
    first_name: str
    dob: date
    height_inches: int
    weight_pounds: int
    eyes_colour: str

"""GET"""

class DriverOut(DriverBase):
    driver_id: int

"""POST"""

# Address Input (Required for the Nested Query)
class AddressCreate(BaseModel):
    zip_code: str
    state: str
    city: str
    street: str
    house: str

# Insert New Driver
class DriverCreate(BaseModel):
    address: AddressCreate
    licence_number: str
    state_issue: str
    last_name: str
    first_name: str
    dob: date
    height_inches: int
    weight_pounds: int
    eyes_colour: str