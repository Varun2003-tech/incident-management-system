from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    service = Column(
        String(255),
        nullable=False
    )

    severity = Column(
        String(10),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False
    )

    owner = Column(
        String(255),
        nullable=True
    )

    summary = Column(
        String(500),
        nullable=True
    )

    createdAt = Column(
        DateTime,
        default=datetime.utcnow
    )

    updatedAt = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
