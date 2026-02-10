# main.py
# Imports
from fastapi import FastAPI
from app.database.db_raw import *
from app.api.routers.drivers import *
from app.api.routers.notices import *

# App Entrypoint
app = FastAPI(
    title="NYPD Road Traffic Notice API",
    version="1.0.0"
)

# Adding Router
app.include_router(drivers_router)
app.include_router(notices_router)

@app.get("/")
async def root():
    """Simple health-check endpoint"""
    return {"message": "App is still running"}