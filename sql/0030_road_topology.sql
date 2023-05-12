CREATE OR REPLACE VIEW road_topology_nodes AS
Select((ST_DumpPoints(geom)).path)[1] as id, (ST_DumpPoints(geom)).geom::geometry(Point, 3857) as geom
from road_endpoints_union;

CREATE OR REPLACE VIEW road_topology_edges AS
(
SELECT row_number() over ()                                               as id,
       s.osm_id                                                           as osm_id,
       split_id                                                           as split_id,
       source.id                                                          as source,
       target.id                                                          as target,
       st_length(s.geom)                                                  as cost,
       CASE When s.oneway = 'yes' THEN -1 ELSE st_length(s.geom) END      as inverse_cost,
       st_length(s.geom)                                                  as length,
       s.geom::geometry(Linestring, 3857)                                 as way,
       st_makeline(source.geom, target.geom) ::geometry(Linestring, 3857) as geom
FROM split_roads s
         left join road_topology_nodes source on st_startpoint(s.geom) = source.geom
         left join road_topology_nodes target on st_endpoint(s.geom) = target.geom
where source.geom is not null
  and target.geom is not null);


