from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    title: str
    company: str
    link: str
    status: str
    applied_date: str # Format: YYYY-MM-DD
    notes: Optional[str] = None