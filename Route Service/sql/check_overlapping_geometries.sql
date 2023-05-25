DROP TABLE IF EXISTS overlapping;
CREATE Table overlapping AS
SELECT distinct st_intersection(t1.way, t2.way)
FROM bike_roads t1,
     bike_roads t2
WHERE t1.osm_id <> t2.osm_id
  AND ST_Intersects(t1.way, t2.way)
  AND Upper(ST_GeometryType(ST_Intersection(t1.way, t2.way))) LIKE '%LINE%';


DROP TABLE IF EXISTS duplicate_geoms;
CREATE TABLE duplicate_geoms AS
Select distinct t1.way
FROM bike_roads t1,
     bike_roads t2
WHERE t1.osm_id <> t2.osm_id
    AND st_equals(t1.way, t2.way);