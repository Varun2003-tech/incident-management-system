from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from . import models


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


def get_incidents(
        db: Session,
        page: int,
        size: int,
        search: str = None,
        severity: str = None,
        status: str = None,
        sort_by: str = "createdAt",
        order: str = "desc"
):

    query = db.query(models.Incident)

    if search:
        query = query.filter(
            models.Incident.title.contains(search)
        )

    if severity:
        query = query.filter(
            models.Incident.severity == severity
        )

    if status:
        query = query.filter(
            models.Incident.status == status
        )

    if order == "asc":
        query = query.order_by(asc(getattr(models.Incident, sort_by)))
    else:
        query = query.order_by(desc(getattr(models.Incident, sort_by)))

    return query.offset(page * size).limit(size).all()


def get_incident(db: Session, id: int):

    return db.query(models.Incident)\
        .filter(models.Incident.id == id)\
        .first()


def update_incident(db: Session, id: int, status: str):

    incident = get_incident(db, id)

    incident.status = status

    db.commit()
    db.refresh(incident)

    return incident
