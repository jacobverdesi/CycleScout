CREATE TABLE IF NOT EXISTS strava_athlete
(
    id bigint primary key not null,
    username varchar,
    resource_state int,
    firstname varchar,
    lastname varchar,
    bio varchar,
    city varchar,
    state varchar,
    country varchar,
    sex varchar,
    premium bool,
    summit bool,
    created_at timestamptz,
    updated_at timestamptz,
    badge_type_id integer,
    weight double precision,
    profile_medium varchar,
    profile varchar,
    friend varchar,
    follower varchar
)
