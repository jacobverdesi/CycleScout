DROP TABLE IF EXISTS goffstown_lines;
CREATE TABLE goffstown_lines AS
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
       ST_Intersection((Select ST_Buffer(way, 1000) from planet_osm_polygon where name = 'Goffstown'), way) AS way
FROM planet_osm_line
WHERE way && ST_BUFFER((Select way from planet_osm_polygon where boundary = 'administrative' and name = 'Goffstown'),1000 )
  AND (bicycle is not null or highway is not null)
;
