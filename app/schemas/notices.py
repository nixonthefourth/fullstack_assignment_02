# app/schemas/notices.py

from pydantic import BaseModel
from datetime import datetime, date

# Notice Base Model
class NoticeBase(BaseModel):
    notice_id: str
    violation_date_time: datetime
    detachment: str
    violation_severity: str
    notice_status: str
    notification_sent: bool
    entry_date: date
    expiry_date: date
    violation_description: str
