from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class StravaToken(Base):
    __tablename__ = "strava_tokens"
    access_token = Column(String, primary_key=True, index=True)
    refresh_token = Column(String)
    expires_at = Column(Integer)
    expires_in = Column(Integer)
    token_type = Column(String)
    athlete_id = Column(Integer, ForeignKey('strava_athlete.id'))
