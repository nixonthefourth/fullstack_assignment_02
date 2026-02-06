# NYPD Notices API
University of Lincoln
Assignment 2, Full Stack Development
Directed, Written and Published by Mykyta "Nick' Khomiakov

## Tech Stack
- Python
- FastAPI
- SQL
- Uvicorn
- Pydantic

## Project Structure
app/
├── main.py
├── routers/
│ └── crud.py
├── models.py
├── db_raw.py
└── notice_base.sql

## Running the project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
