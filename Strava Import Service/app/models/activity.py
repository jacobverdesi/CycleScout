from sqlalchemy import Column, Integer, String, Boolean, Float, BigInteger, DateTime

from app.db.database import Base


class Activity(Base):
    __tablename__ = "strava_activities"
    id = Column(BigInteger, primary_key=True, index=True)
    external_id = Column(String)
    upload_id = Column(BigInteger)
    athlete_id = Column(Integer)
    name = Column(String)
    distance = Column(Float)
    moving_time = Column(Integer)
    elapsed_time = Column(Integer)
    total_elevation_gain = Column(Float)
    elev_high = Column(Float)
    elev_low = Column(Float)
    type = Column(String)
    sport_type = Column(String)
    start_date = Column(DateTime)
    start_date_local = Column(DateTime)
    timezone = Column(String)
    start_latlng = Column(String)
    end_latlng = Column(String)
    achievement_count = Column(Integer)
    kudos_count = Column(Integer)
    comment_count = Column(Integer)
    athlete_count = Column(Integer)
    photo_count = Column(Integer)
    total_photo_count = Column(Integer)
    map = Column(String)
    trainer = Column(Boolean)
    commute = Column(Boolean)
    manual = Column(Boolean)
    private = Column(Boolean)
    flagged = Column(Boolean)
    workout_type = Column(Integer)
    average_speed = Column(Float)
    max_speed = Column(Float)
    has_kudoed = Column(Boolean)
    gear_id = Column(String)
    kilojoules = Column(Float)
    average_watts = Column(Float)
    device_watts = Column(Boolean)
    max_watts = Column(Integer)
    weighted_average_watts = Column(Integer)


# id,
# external_id,
# upload_id,
# upload_id_str,
# athlete,
# name,
# distance,
# moving_time,
# elapsed_time,
# total_elevation_gain,
# elev_high,
# elev_low,
# type,
# sport_type,
# workout_type,
# start_date,
# start_date_local,
# timezone,
# utc_offset,
# location_city,
# location_state,
# location_country,
# start_latlng,
# end_latlng,
# achievement_count,
# has_kudoed,
# kudos_count,
# comment_count,
# athlete_count,
# photo_count,
# total_photo_count,
# map,
# trainer,
# commute,
# manual,
# private,
# visibility,
# flagged,
# gear_id,
# average_speed,
# max_speed,
# average_watts,
# kilojoules,
# device_watts,
# has_heartrate,
# heartrate_opt_out,
# max_heartrate,
# average_heartrate,
# display_hide_heartrate_option,
# resource_state,
# from_accepted_tag,
# pr_count,
# suffer_score
