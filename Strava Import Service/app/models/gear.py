from sqlmodel import Field, SQLModel



class SummaryGear(SQLModel):
    id: str = Field(primary_key=True)
    resource_state: int = Field(default=None, nullable=True)
    primary: bool = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=True)
    distance: float = Field(default=None, nullable=True)


class DetailedGear(SummaryGear):
    brand_name: str = Field(default=None, nullable=True)
    model_name: str = Field(default=None, nullable=True)
    frame_type: int = Field(default=None, nullable=True)
    description: str = Field(default=None, nullable=True)


class Gear(DetailedGear, table=True):
    pass
