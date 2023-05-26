from pydantic import BaseModel


class Activity(BaseModel):
    id: int
    external_id: str
    upload_id: int
    upload_id_str: str
    athlete_id: int
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    elev_high: float
    elev_low: float
    type: str
    sport_type: str
    workout_type: int
    start_date: str
    start_date_local: str
    timezone: str
    utc_offset: int
    location_city: str
    location_state: str
    location_country: str
    start_latlng: str
    end_latlng: str
    achievement_count: int
    has_kudoed: bool
    kudos_count: int
    comment_count: int
    athlete_count: int
    photo_count: int
    total_photo_count: int
    map: str
    trainer: bool
    commute: bool
    manual: bool
    private: bool
    visibility: str
    flagged: bool
    gear_id: str
    average_speed: float
    max_speed: float
    average_watts: float
    kilojoules: float
    device_watts: bool
    has_heartrate: bool
    heartrate_opt_out: bool
    max_heartrate: int
    average_heartrate: int




    class Config:
        orm_mode = True