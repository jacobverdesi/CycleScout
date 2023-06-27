
import time

from fastapi import APIRouter, Depends, logger
from select import select

from app.config import Settings
from app.core import strava_api
from app.core.strava_api import strava_api_client
from app.db import crud
from app.db.database import engine, EntityJsonB
from sqlmodel import Session
router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/save_activities")
def save_activities(athlete_id: int = 45406272,page:int =1, db: Session = Depends(get_session)):
    strava_token = crud.get_strava_token(db, athlete_id)
    strava_api_client.access_token = strava_token.access_token
    if strava_token is not None:
        activities = strava_api_client.get_activities()
        for activity in activities:

            # db_activity = crud.get_entitys(db, select(EntityJsonB).where(EntityJsonB.id == activity.id))
            # if db_activity is None:
            crud.create_entity(db, activity)

        return {"message": "Activities saved"}
    return {"message": "No token found"}

