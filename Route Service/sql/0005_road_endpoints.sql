DROP TABLE IF EXISTS road_endpoints_union;
CREATE TABLE road_endpoints_union
(
    id   serial NOT NULL PRIMARY KEY,
    geom geometry(MultiPoint, 3857)
);
CREATE INDEX road_endpoints_union_geom_idx ON road_endpoints_union USING GIST (geom);

INSERT INTO road_endpoints_union (geom)
SELECT ST_CollectionExtract(ST_Collect(intersection_points.geom), 1) AS multipoint_geom
FROM (SELECT DISTINCT (ST_Dump(ST_Intersection(a.way, b.way))).geom AS geom
      FROM bike_roads a,
           bike_roads b
      WHERE a.osm_id < b.osm_id
        AND ST_Intersects(a.way, b.way)
        AND a.layer = b.layer
      UNION
      SELECT DISTINCT st_startpoint(way) as geom
      FROM bike_roads
      WHERE st_startpoint(way) IS NOT NULL
      UNION
      SELECT DISTINCT st_endpoint(way) as geom
      FROM bike_roads
      WHERE st_endpoint(way) IS NOT NULL) AS intersection_points;

