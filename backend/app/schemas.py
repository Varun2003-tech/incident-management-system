from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Used for creating incident
class IncidentCreate(BaseModel):

    title: str
    service: str
    severity: str
    status: str
    owner: Optional[str] = "Admin"
    summary: Optional[str] = ""


# ✅ ADD THIS CLASS (missing one)
class IncidentUpdate(BaseModel):

    status: str


# Used for response
class IncidentResponse(BaseModel):

    id: int
    title: str
    service: str
    severity: str
    status: str
    owner: Optional[str]
