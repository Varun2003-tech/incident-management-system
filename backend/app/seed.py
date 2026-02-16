from .database import SessionLocal
from .models import Incident
import random


def seed_data():

    db = SessionLocal()

    severities = ["SEV1", "SEV2", "SEV3", "SEV4"]
    statuses = ["OPEN", "MITIGATED", "RESOLVED"]

    for i in range(200):

        incident = Incident(
            title=f"Incident {i}",
            service="Payment Service",
            severity=random.choice(severities),
            status=random.choice(statuses),
            owner="Admin",
            summary="Sample incident summary"
        )

        db.add(incident)

    db.commit()
    db.close()

    print("Seeded 200 incidents")
