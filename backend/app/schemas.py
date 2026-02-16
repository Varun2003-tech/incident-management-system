from pydantic import BaseModel
from datetime import datetime


class IncidentCreate(BaseModel):

    title: str
    service: str
    severity: str
    status: str
    owner: str | None = None
    summary: str | None = None


class IncidentUpdate(BaseModel):

    status: str


class IncidentResponse(BaseModel):

    id: int
    title: str
    service: str
    severity: str
    status: str
    owner: str | None
    summary: str | None
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
