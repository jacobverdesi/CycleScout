import uuid

from pydantic import BaseModel
from sqlmodel import Session

from app.db.database import EntityJsonB, StravaToken


def create_entity(db: Session, model: BaseModel):
    db_entity = EntityJsonB.from_model(model)
    db.add(db_entity)
    db.commit()


def get_entitys(db: Session, statement):
    return db.exec(statement).first()


def get_entity_by_uuid(db: Session, id: uuid.UUID):
    return db.get(EntityJsonB, id)


def delete_entity(db: Session, id: uuid.UUID):
    db_entity = db.get(EntityJsonB, id)
    db.delete(db_entity)
    db.commit()


def update_entity(db: Session, id: uuid.UUID, model: BaseModel):
    db_entity = db.get(EntityJsonB, id)
    db_entity.data = model.dict()
    db.commit()
    db.refresh(db_entity)
    return db_entity


def create_strava_token(db: Session, strava_token: StravaToken):
    db.add(strava_token)
    db.commit()
def update_strava_token(db: Session, strava_token: StravaToken):
    db_strava_token = db.get(StravaToken, strava_token.athlete_id)
    db_strava_token.access_token = strava_token.access_token
    db_strava_token.refresh_token = strava_token.refresh_token
    db_strava_token.expires_at = strava_token.expires_at
    db.commit()
    db.refresh(db_strava_token)
    return db_strava_token


def get_strava_token(db: Session, athlete_id: int):
    return db.get(StravaToken, athlete_id)
