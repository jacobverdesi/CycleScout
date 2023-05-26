import json
import os
import time

import requests
from fastapi import APIRouter, Depends, logger
from sqlalchemy.orm import Session

from app.config import Settings
from app.core import strava_api
from app.db import crud
from app.db.database import SessionLocal
from app.schemas import Activity
from app.schemas.athlete import Athlete
from app.schemas.strava_token import StravaToken

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/strava_subscribe/{code}")
def strava_subscribe(code: int, db: Session = Depends(get_db)):
    # response = requests.post(
    #     url='https://www.strava.com/oauth/token',
    #     data={
    #         'client_id': Settings.client_id,
    #         'client_secret': Settings.client_secret,
    #         'code': f'{code}',
    #         'grant_type': 'authorization_code'
    #     }
    # )
    # strava_tokens = response.json()

    strava_token = json.load(open(os.getcwd() + "/routers/strava_tokens.json", 'r'))
    print(strava_token)
    athlete = Athlete(**strava_token['athlete'])
    strava_token['athlete_id'] = athlete.id
    strava_token = StravaToken(**strava_token)
    db_athlete = crud.get_athlete(db, athlete.id)
    if db_athlete is None:
        crud.create_athlete(db, athlete)
        crud.create_strava_token(db, strava_token)
        return {"message": "Athlete created"}
    else:
        return {"message": "Athlete already exists"}


@router.post("/save_activities")
def save_activities(athlete_id: int = 45406272,page:int =1, db: Session = Depends(get_db)):
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


@router.get("/strava_auth", response_model=StravaToken)
def strava_auth(athlete_id: int = 45406272, db: Session = Depends(get_db)):
    strava_token = crud.get_strava_token(db, athlete_id)

    return strava_token
