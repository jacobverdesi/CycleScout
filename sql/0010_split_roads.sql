DROP TABLE IF EXISTS road_endpoints;
CREATE TABLE road_endpoints
(
    id   serial NOT NULL PRIMARY KEY,
    geom geometry(Point, 3857)
);

INSERT INTO road_endpoints (geom)
SELECT DISTINCT st_startpoint(way) as geom
FROM bike_roads
where st_startpoint(way) is not null
UNION
SELECT DISTINCT st_endpoint(way) as geom
FROM bike_roads
where  st_endpoint(way) is not null;


DROP TABLE IF EXISTS road_segments;
CREATE TABLE road_segments
(
    id   serial NOT NULL PRIMARY KEY,
    geom geometry(LineString, 3857)
);
INSERT INTO road_segments (geom)
SELECT sp, ep
FROM road_endpoints sp
JOIN road_endpoints ep ON ST_Touches(sp.geom, ep.geom) AND sp.id = ep.id
--JOIN bike_roads lt ON ST_Intersects(lt.way, sp.geom) AND ST_Intersects(lt.way, ep.geom);



