import uvicorn
from fastapi import FastAPI, APIRouter

from app.routers import strava_auth

app = FastAPI()

api_router = APIRouter()
api_router.include_router(strava_auth.router, tags=["login"])

app.include_router(api_router, prefix="/api")

if __name__ == '__main__':
    uvicorn.run("app.main:app",reload=True, host="0.0.0.0", port=8080)