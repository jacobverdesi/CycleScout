DROP TABLE IF EXISTS goffstown_road_network_nodes;
CREATE TABLE goffstown_road_network_nodes
(
    id     serial NOT NULL PRIMARY KEY,
    way_id bigint NOT NULL,
    geom   geometry(Point, 3857)
);
INSERT INTO goffstown_road_network_nodes (way_id, geom)
SELECT osm_id, st_startpoint(way) as geom
FROM goffstown_bike_roads;

INSERT INTO goffstown_road_network_nodes (way_id, geom)
SELECT osm_id,st_endpoint(way) as geom
FROM goffstown_bike_roads;



--
-- INSERT INTO goffstown_road_network_nodes (geom)
-- SELECT st_intersection(source.way, target.way) as geom
-- FROM goffstown_bike_roads source,
--      goffstown_bike_roads target
-- WHERE source.osm_id > target.osm_id
--   and st_touches(source.way, target.way)