from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, or_
from . import models
from fastapi import FastAPI, HTTPException, Depends



# CREATE INCIDENT
def create_incident(db: Session, incident):

    db_incident = models.Incident(
        title=incident.title,
        service=incident.service,
        severity=incident.severity,
        status=incident.status,
        owner=incident.owner,
        summary=incident.summary
    )

    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)

    return db_incident


# GET INCIDENTS (Pagination + Search + Filter + Sort)
def get_incidents(
    db: Session,
    page: int = 0,
    size: int = 10,
    search: str = None,
    severity: str = None,
    status: str = None,
    sort_by: str = "createdAt",
    order: str = "desc"
):

    query = db.query(models.Incident)

    # SEARCH (case-insensitive, supports title and service)
    if search:
        query = query.filter(
            or_(
                models.Incident.title.ilike(f"%{search}%"),
                models.Incident.service.ilike(f"%{search}%")
            )
        )

    # FILTER BY SEVERITY
    if severity:
        query = query.filter(
            models.Incident.severity == severity
        )

    # FILTER BY STATUS
    if status:
        query = query.filter(
            models.Incident.status == status
        )

    # SAFE SORT COLUMN
    allowed_sort_fields = [
        "id",
        "title",
        "service",
        "severity",
        "status",
        "createdAt",
        "updatedAt"
    ]

    if sort_by not in allowed_sort_fields:
        sort_by = "createdAt"

    sort_column = getattr(models.Incident, sort_by)

    # SORT ORDER
    if order == "asc":
        query = query.order_by(asc(sort_column))
    else:
        query = query.order_by(desc(sort_column))

    # PAGINATION
    incidents = query.offset(page * size).limit(size).all()

    return incidents


# GET SINGLE INCIDENT
def get_incident(db: Session, id: int):

    return db.query(models.Incident)\
        .filter(models.Incident.id == id)\
        .first()


# UPDATE INCIDENT STATUS
def update_incident(db: Session, id: int, status: str):

    incident = db.query(models.Incident)\
        .filter(models.Incident.id == id)\
        .first()

    if not incident:
       raise HTTPException(status_code=404, detail="Incident not found")


    incident.status = status

    db.commit()
    db.refresh(incident)

    return incident
