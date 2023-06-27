
import time

from fastapi import APIRouter, Depends, logger

from app.config import Settings
from app.core import strava_api
from app.db import crud
from app.db.database import engine
from sqlmodel import Session
router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session
#
# @router.put("/update_athlete"):
# def update_athlete(athlete_id: int = 45406272, db: Session = Depends(get_session)):
#
#


# @router.post("/strava_subscribe/{code}")
# def strava_subscribe(code: int, db: Session = Depends(get_session)):
#     # response = requests.post(
#     #     url='https://www.strava.com/oauth/token',
#     #     data={
#     #         'client_id': Settings.client_id,
#     #         'client_secret': Settings.client_secret,
#     #         'code': f'{code}',
#     #         'grant_type': 'authorization_code'
#     #     }
#     # )
#     # strava_tokens = response.json()
#
#     strava_token = json.load(open(os.getcwd() + "/routers/strava_tokens.json", 'r'))
#     print(strava_token)
#     athlete = SummaryAthlete(**strava_token['athlete'])
#     strava_token['athlete_id'] = athlete.id
#     strava_token = StravaToken(**strava_token)
#     db_athlete = crud.get_athlete(db, athlete.id)
#     if db_athlete is None:
#         crud.create_athlete(db, athlete)
#         crud.create_strava_token(db, strava_token)
#         return {"message": "Athlete created"}
#     else:
#         return {"message": "Athlete already exists"}


