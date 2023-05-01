DROP TABLE IF EXISTS road_network_nodes;
CREATE TABLE road_network_nodes
(
    id     serial NOT NULL PRIMARY KEY,
    way_id bigint NOT NULL,
    geom   geometry(Point, 3857)
);
DROP TABLE IF EXISTS road_network_edges;
CREATE TABLE road_network_edges
(
    id     serial NOT NULL PRIMARY KEY,
    way_id bigint NOT NULL,
    length double precision,
    geom   geometry(Linestring, 3857)
);

INSERT INTO road_network_nodes (way_id, geom)
SELECT osm_id, st_startpoint(way) as geom
FROM bike_roads;

INSERT INTO road_network_nodes (way_id, geom)
SELECT osm_id,st_endpoint(way) as geom
FROM bike_roads;

INSERT INTO road_network_edges ( way_id,length, geom)
SELECT osm_id,st_length(way), st_makeline(st_startpoint(way), st_endpoint(way)) as geom
FROM bike_roads;


