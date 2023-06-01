import json
import os
import time
from typing import Annotated

from fastapi import APIRouter
from starlette import status
from starlette.responses import RedirectResponse

from stravalib.client import Client
from app.config import settings

router = APIRouter(include_in_schema=False)


@router.post("/authorize", response_class=RedirectResponse, include_in_schema=False)
async def authorize():
    client = Client()
    authorize_url = client.authorization_url(client_id=settings.client_id,
                                             redirect_uri=f"http://{settings.host}:{settings.port}/authorized")
    return RedirectResponse(authorize_url, status_code=status.HTTP_302_FOUND)


@router.get("/authorized", response_class=RedirectResponse, include_in_schema=False)
async def authorized(state: str, code: str, scope: str):
    print(f"{state}, {code}, {scope}")
    return RedirectResponse(f"http://{settings.host}:{settings.port}/docs", status_code=status.HTTP_302_FOUND)
