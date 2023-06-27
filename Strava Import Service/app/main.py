import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.templating import Jinja2Templates
from stravalib import Client

from app.routers import root,strava_auth, athletes, activities

app = FastAPI()

api_router = APIRouter()
api_router.include_router(athletes.router, tags=["Athletes"])
api_router.include_router(activities.router, tags=["Activities"])

app.include_router(root.router)
app.include_router(strava_auth.router)

app.include_router(api_router, prefix="/api")



# @app.on_event("startup")
# def on_startup():
#     # get schema from db
#     # compare schema to models
#     # if schema is different, update db
#
#     create_db_tables_index()


if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)
