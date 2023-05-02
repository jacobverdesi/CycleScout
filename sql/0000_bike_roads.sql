DROP TABLE IF EXISTS bike_roads;
CREATE TABLE bike_roads AS
SELECT osm_id,
       access,
       bicycle,
       bridge,
       construction,
       foot,
       highway,
       horse,
       junction,
       coalesce(layer, '0') as layer,
       name,
       oneway,
       railway,
       ref,
       route,
       surface,
       tracktype,
       z_order,
       way
FROM planet_osm_line
WHERE (access not in ('private', 'customers', 'military','no') or access is null)                 -- private access
  AND (bicycle not in ('dismount', 'use_sidepath', 'private', 'no') or bicycle is null)      -- private bicycle
  AND osm_id not in (Select osm_id from planet_osm_line group by osm_id having count(*) > 1) -- duplicate ways


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
CREATE INDEX bike_roads_way_idx ON bike_roads USING gist(way);

DELETE FROM bike_roads WHERE osm_id IN
(Select t2.osm_id FROM bike_roads t1,
     bike_roads t2
WHERE t1.osm_id <> t2.osm_id
    AND st_equals(t1.way, t2.way))

