from sqlalchemy.orm import Session

from app import models, schemas

schemas.Athlete.__tablename__ = "strava_athlete"


def create_athlete(db: Session, athlete: schemas.Athlete):
    db_athlete = models.Athlete(**athlete.dict())
    db.add(db_athlete)
    db.commit()
    db.refresh(db_athlete)
    return db_athlete


def get_athlete(db: Session, athlete_id: int):
    # noinspection PyTypeChecker
    return db.query(models.Athlete).filter(models.Athlete.id == athlete_id).first()


def create_strava_token(db: Session, strava_token: schemas.StravaToken):
    db_strava_token = models.StravaToken(**strava_token.dict())
    db.add(db_strava_token)
    db.commit()
    db.refresh(db_strava_token)
    return db_strava_token


def get_strava_token(db: Session, athlete_id: int):
    # noinspection PyTypeChecker
    return db.query(models.StravaToken).filter(models.StravaToken.athlete_id == athlete_id).order_by(models.StravaToken.expires_at.desc()).first()


def create_activity(db:Session, activity: schemas.Activity):
    db_activity = models.Activity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity