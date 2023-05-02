DROP TABLE IF EXISTS road_network_nodes;
CREATE TABLE road_network_nodes
(
    id   serial NOT NULL PRIMARY KEY,
    geom geometry(Point, 3857)
);
DROP TABLE IF EXISTS road_network_edges;
CREATE TABLE road_network_edges
(
    id       serial  NOT NULL PRIMARY KEY,
    source   integer NOT NULL,
    target   integer NOT NULL,
    osm_id   bigint  NOT NULL,
    split_id bigint  NOT NULL,
    length   double precision,
    geom     geometry(Linestring, 3857)
);
INSERT INTO road_network_nodes (geom)
Select (ST_DumpPoints(geom)).geom
from road_endpoints_union;

INSERT INTO road_network_edges (source, target, osm_id, split_id, length, geom)
    (SELECT source.id, target.id, s.osm_id, split_id, st_length(s.geom),st_makeline(source.geom, target.geom)
     FROM split_roads s
              left join road_network_nodes source on st_startpoint(s.geom) = source.geom
              left join road_network_nodes target on st_endpoint(s.geom) = target.geom
     where source.geom is not null
       and target.geom is not null);


