import uuid
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import create_engine, Index
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base
from sqlmodel import SQLModel, Field

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

class StravaToken(SQLModel, table=True):
    athlete_id: int = Field(default=None,primary_key=True)
    access_token: str
    refresh_token: str
    expires_at: int
class EntityJsonB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str = Field(default="entity")
    data: dict = Field(default={}, sa_column=Column(JSONB))

    @classmethod
    def from_model(cls, model: BaseModel):
        # make datetime objects json serializable
        data = model.dict()
        for key, value in model.dict().items():
            if isinstance(value, datetime.datetime):
                data[key] = value.isoformat()
        return cls(type=model.__class__.__name__, data=data)

    class Config:
        arbitrary_types_allowed = True


def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
