from sqlmodel import Session

from app import models


def create_athlete(db: Session, athlete: models.MetaAthlete | models.SummaryAthlete | models.DetailedAthlete):
    athlete = models.Athlete(**athlete.dict())
    db.add(athlete)
    db.commit()
    db.refresh(athlete)
    return athlete


def get_athlete(db: Session, id: int, resource_state: int = 2):
    athlete = db.get(models.Athlete,id)
    return athlete
def delete_athlete(db: Session, id: int):
    athlete = db.get(models.Athlete,id)
    db.delete(athlete)
    db.commit()
    return athlete
def create_strava_token(db: Session, strava_token: models.StravaToken):
    db_strava_token = models.StravaToken(**strava_token.dict())
    db.add(db_strava_token)
    db.commit()
    db.refresh(db_strava_token)
    return db_strava_token


def get_strava_token(db: Session, athlete_id: int):
    # noinspection PyTypeChecker
    return db.query(models.StravaToken).filter(models.StravaToken.athlete_id == athlete_id).order_by(
        models.StravaToken.expires_at.desc()).first()

# def create_activity(db:Session, activity: schemas.Activity):
#     db_activity = models.Activity(**activity.dict())
#     db.add(db_activity)
#     db.commit()
#     db.refresh(db_activity)
#     return db_activity

if __name__ == '__main__':
    from app.db.database import engine



    db=Session(engine)
    delete_athlete(db ,45406272)