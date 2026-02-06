# main.py
# Imports
from fastapi import FastAPI
from db_raw import *
from models import *
from routers import crud

# App Entrypoint
app = FastAPI(
    title="NYPD API",
    version="1.0.0"
)

# Adding Router
app.include_router(crud.router)

@app.get("/")
async def root():
    """Simple health-check endpoint."""
    return {"message": "App is still running"}