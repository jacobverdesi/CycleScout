import datetime
from typing import List

from sqlmodel import Field, SQLModel, Relationship
from app.models import StravaToken
from app.models.gear import SummaryGear


class MetaAthlete(SQLModel):
    id: int = Field(primary_key=True)


class SummaryAthlete(MetaAthlete):
    resource_state: int = Field(default=None, nullable=True)
    firstname: str = Field(default=None, nullable=True)
    lastname: str = Field(default=None, nullable=True)
    profile_medium: str = Field(default=None, nullable=True)
    profile: str = Field(default=None, nullable=True)
    city: str = Field(default=None, nullable=True)
    state: str = Field(default=None, nullable=True)
    country: str = Field(default=None, nullable=True)
    sex: str = Field(default=None, nullable=True)
    premium: bool = Field(default=None, nullable=True)
    summit: bool = Field(default=None, nullable=True)
    created_at: datetime.datetime = Field(default=None, nullable=True)
    updated_at: datetime.datetime = Field(default=None, nullable=True)


class DetailedAthlete(SummaryAthlete):
    follower_count: int = Field(default=None, nullable=True)
    friend_count: int = Field(default=None, nullable=True)
    measurement_preference: str = Field(default=None, nullable=True)
    ftp: int = Field(default=None, nullable=True)
    weight: float = Field(default=None, nullable=True)
    bikes: List[SummaryGear] = Relationship(back_populates="athlete")
    shoes: List[SummaryGear] = Relationship(back_populates="athlete")


class Athlete(DetailedAthlete, table=True):
    tokens: List[StravaToken] = Relationship(sa_relationship_kwargs={"cascade": "all,delete, delete-orphan"})
