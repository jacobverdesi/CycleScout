from typing import TYPE_CHECKING

from pydantic import BaseModel


class StravaToken(BaseModel):
    access_token: str
    refresh_token: str
    expires_at: int
    expires_in: int
    token_type: str
    athlete_id: int

    class Config:
        orm_mode = True