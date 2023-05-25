import requests
from fastapi import APIRouter

from app.config import Settings

router = APIRouter()


@router.post("/")
def strava_auth(code: int):
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': Settings.client_id,
            'client_secret': Settings.client_secret,
            'code': f'{code}',
            'grant_type': 'authorization_code'
        }
    )
    strava_tokens = response.json()

    return {"message": "Hello World"}
