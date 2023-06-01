
import time

from fastapi import APIRouter, Depends, logger

from app.config import Settings
from app.core import strava_api
from app.db import crud
from app.db.database import engine
from app.models import StravaToken, SummaryAthlete
from sqlmodel import Session
router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/save_activities")
def save_activities(athlete_id: int = 45406272,page:int =1, db: Session = Depends(get_session)):
    strava_token = crud.get_strava_token(db, athlete_id)
    token_exipred = strava_token.expires_at - time.time() < 0
    if token_exipred:
        # call refresh token
        logger.logger.info("Token expired, refreshing")
        strava_token = strava_api.get_refresh_token(strava_token.refresh_token)
        strava_token['athlete_id'] = athlete_id
        strava_token = StravaToken(**strava_token)
        crud.create_strava_token(db, strava_token)

    if strava_token is not None:
        activities = strava_api.get_activities(strava_token.access_token,page)
        for activity in activities:
            activity['athlete_id'] = athlete_id
            activity['start_latlng'] = str(activity['start_latlng'])
            activity['end_latlng'] = str(activity['end_latlng'])
            activity['map'] = str(activity['map']['summary_polyline'])
            activity = Activity(**activity)
            crud.create_activity(db, activity)
        return {"message": "Activities saved"}
    return {"message": "No token found"}

