CREATE TABLE bike_table (
    osm_id bigint,
    access text,
    bicycle text,
    bridge text,
    construction text,
    foot text,
    highway text,
    horse text,
    junction text,
    layer text,
    name text,
    oneway text,
    railway text,
    ref text,
    route text,
    surface text,
    tracktype text,
    z_order integer,
    way geometry(LineString,3857)
);
CREATE TABLE filter_boundary() INHERITS (bike_table);
CREATE TABLE filter_duplicate_osm_ids() INHERITS (bike_table);
CREATE TABLE filter_() INHERITS (bike_table);
CREATE TABLE filter_boundary() INHERITS (bike_table);

ALTER TABLE tbl_b INHERIT bike_table;
ALTER TABLE tbl_c INHERIT bike_table;
ALTER TABLE tbl_d INHERIT bike_table;


DROP TABLE IF EXISTS filter_boundary;
CREATE TABLE filter_boundary AS
SELECT osm_id,
       access,
       bicycle,
       bridge,
       construction,
       foot,
       highway,
       horse,
       junction,
       layer,
       name,
       oneway,
       railway,
       ref,
       route,
       surface,
       tracktype,
       z_order,
       ST_Intersection((Select way from planet_osm_polygon where name = :boundry_name), way) AS way
FROM planet_osm_line
WHERE way && (Select way from planet_osm_polygon where boundary = 'administrative' and name = :boundry_name);

DROP TABLE IF EXISTS filter_duplicate;

CREATE TABLE filter_duplicate AS
SELECT *
from filter_boundary
WHERE osm_id not in (Select osm_id from planet_osm_line group by osm_id having count(*) > 1)
DROP TABLE IF EXISTS filter_private;
CREATE TABLE filter_private AS

SELECT *
FROM filter_duplicate
WHERE (access not in ('private', 'customers', 'military') or access is null) -- private access
  AND (bicycle not in ('dismount', 'use_sidepath', 'private', 'no') or bicycle is null);



DROP TABLE IF EXISTS goffstown_road_network;
CREATE TABLE goffstown_road_network AS
SELECT osm_id,
       access,
       bicycle,
       bridge,
       construction,
       foot,
       highway,
       horse,
       junction,
       layer,
       name,
       oneway,
       railway,
       ref,
       route,
       surface,
       tracktype,
       z_order,
       ST_Intersection((Select ST_Buffer(way,1) from planet_osm_polygon where name = 'Goffstown'), way) AS way
FROM planet_osm_line
WHERE way && (Select way from planet_osm_polygon where boundary = 'administrative' and name = 'Goffstown') -- Goffstown
  AND (access not in ('private', 'customers', 'military') or access is null)                               -- private access
  AND (bicycle not in ('dismount', 'use_sidepath', 'private', 'no') or bicycle is null)                    -- private bicycle
  AND osm_id not in (Select osm_id from planet_osm_line group by osm_id having count(*) > 1)               -- duplicate ways


--    OR highway = 'cycleway'
  AND ((bicycle in ('yes', 'designate', 'permissive', 'official')
    OR highway not in ('motorway', 'motorway_link', 'steps', 'stairs', 'escalator', 'elevator', 'construction',
                       'proposed', 'demolished', 'escape', 'bus_guideway', 'sidewalk', 'crossing', 'bus_stop',
                       'traffic_signals', 'stop', 'give_way', 'milestone', 'platform', 'speed_camera',
                       'elevator',
                       'raceway', 'rest_area', 'traffic_island', 'services', 'yes', 'no', 'drain',
                       'street_lamp',
                       'razed', 'corridor', 'busway', 'via_ferrata',
                       'trunk', 'trunk_link', 'footway', 'service', 'bridleway'))
    );

