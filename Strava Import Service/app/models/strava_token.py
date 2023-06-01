from sqlmodel import Field, SQLModel, Relationship



class StravaToken(SQLModel, table=True):
    access_token: str = Field(primary_key=True)
    refresh_token: str = Field(default=None, nullable=True)
    expires_at: int = Field(default=None, nullable=True)
    expires_in: int = Field(default=None, nullable=True)
    token_type: str = Field(default=None, nullable=True)
    athlete_id: int = Field(foreign_key="athlete.id")
    #athlete: Athlete = Relationship(back_populates="tokens")