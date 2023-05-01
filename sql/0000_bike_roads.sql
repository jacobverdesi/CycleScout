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
       layer,
       name,
       oneway,
       railway,
       ref,
       route,
       surface,
       tracktype,
       z_order,
       way
FROM goffstown_lines
WHERE (access not in ('private', 'customers', 'military') or access is null)                 -- private access
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

