from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import schemas, crud, seed

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Incident Tracker API"
)


@app.on_event("startup")
def startup():

    seed.seed_data()


@app.post("/api/incidents")
def create_incident(
        incident: schemas.IncidentCreate,
        db: Session = Depends(get_db)
):

    return crud.create_incident(db, incident)


@app.get("/api/incidents")
def get_incidents(
        page: int = 0,
        size: int = 10,
        search: str = None,
        severity: str = None,
        status: str = None,
        sort_by: str = "createdAt",
        order: str = "desc",
        db: Session = Depends(get_db)
):

    return crud.get_incidents(
        db,
        page,
        size,
        search,
        severity,
        status,
        sort_by,
        order
    )


@app.get("/api/incidents/{id}")
def get_incident(
        id: int,
        db: Session = Depends(get_db)
):

    return crud.get_incident(db, id)


@app.patch("/api/incidents/{id}")
def update_incident(
        id: int,
        incident: schemas.IncidentUpdate,
        db: Session = Depends(get_db)
):

    return crud.update_incident(
        db,
        id,
        incident.status
    )
