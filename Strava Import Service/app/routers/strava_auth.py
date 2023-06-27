import json
import os
import time
from typing import Annotated

import stravalib
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from starlette import status
from starlette.responses import RedirectResponse

from app.config import settings
from app.core.strava_api import strava_api_client
from app.db import crud
from app.db.database import engine, StravaToken, EntityJsonB

router = APIRouter(include_in_schema=False)


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/authorize", response_class=RedirectResponse, include_in_schema=False)
async def authorize():
    authorize_url = strava_api_client.authorization_url(client_id=settings.client_id,
                                                        redirect_uri=f"http://{settings.host}:{settings.port}/authorized")
    return RedirectResponse(authorize_url, status_code=status.HTTP_302_FOUND)


@router.get("/authorized", response_class=RedirectResponse, include_in_schema=False)
async def authorized(state: str, code: str, scope: str, db: Session = Depends(get_session)):
    print(f"{state}, {code}, {scope}")
    strava_token = strava_api_client.exchange_code_for_token(client_id=settings.client_id,
                                                             client_secret=settings.client_secret, code=code)
    strava_api_client.access_token = strava_token['access_token']
    athlete = strava_api_client.get_athlete()
    athlete = EntityJsonB.from_model(athlete)
    db_athlete = crud.get_entitys(db, select(EntityJsonB).where(EntityJsonB.data['id'] == '45406272'))
    if db_athlete is None:
        crud.create_entity(db, athlete)
    elif athlete.data != db_athlete.data:
        print(f"Updating athlete {db_athlete.data['id']}")
        athlete = crud.update_entity(db, athlete.id, athlete)
    db_strava_token = crud.get_strava_token(db, athlete.data['id'])
    strava_token['athlete_id'] = athlete.data['id']
    strava_token = StravaToken(**strava_token)
    if db_strava_token is None:
        crud.create_strava_token(db, strava_token)
    elif strava_token != db_strava_token:
        print(f"Updating token for athlete {athlete.data['id']}")
        crud.update_strava_token(db, strava_token)

    return RedirectResponse(f"http://{settings.host}:{settings.port}/docs", status_code=status.HTTP_302_FOUND)
