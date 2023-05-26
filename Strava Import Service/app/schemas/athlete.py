from pydantic import BaseModel


class Athlete(BaseModel):
    id: int
    username: str
    resource_state: int
    firstname: str
    lastname: str
    bio: str = None
    city: str
    state: str
    country: str
    sex: str
    premium: bool
    summit: bool
    created_at: str
    updated_at: str
    badge_type_id: int
    weight: float
    profile_medium: str
    profile: str
    friend: str = None
    follower: str = None

