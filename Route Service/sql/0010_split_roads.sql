DROP TABLE IF EXISTS split_roads;
CREATE TABLE split_roads
AS
SELECT r.osm_id,
        r.access,
        r.bicycle,
        r.bridge,
        r.construction,
        r.foot,
        r.highway,
        r.horse,
        r.junction,
        r.layer,
        r.name,
        r.oneway,
        r.railway,
        r.ref,
        r.route,
        r.surface,
        r.tracktype,
        r.z_order,
        (ST_DUMP(ST_Split(r.way, s.geom))).path[1] as split_id,
        (ST_DUMP(ST_Split(r.way, s.geom))).geom as geom
FROM bike_roads r,
     road_endpoints_union s;




