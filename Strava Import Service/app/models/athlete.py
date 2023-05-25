from sqlalchemy import Column, Integer, String, Boolean, Float


class Athlete:
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True),
    resource_state = Column(Integer),
    firstname = Column(String),
    lastname = Column(String),
    bio = Column(String, nullable=True),
    city = Column(String),
    state = Column(String),
    country = Column(String),
    sex = Column(String),
    premium = Column(Boolean),
    summit = Column(Boolean),
    created_at = Column(String),
    updated_at = Column(String),
    badge_type_id = Column(Integer),
    weight = Column(Float),
    profile_medium = Column(String),
    profile = Column(String),
    friend = Column(String, nullable=True),
    follower = Column(String, nullable=True)
