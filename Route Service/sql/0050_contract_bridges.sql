CREATE OR REPLACE VIEW road_network_bridge AS
SELECT e.*,
       CASE
           WHEN e.id
               in (Select *
                   from pgr_bridges(
                           'SELECT id, source, target, length as cost FROM road_topology_edges_connected'
                       ))
               THEN 1
           ELSE 0
           END AS bridge
FROM road_topology_edges_connected e;


CREATE OR REPLACE VIEW road_topology_no_bridge AS
SELECT e.*
FROM road_topology_edges_connected e
WHERE e.id
      not in (Select *
              from pgr_bridges(
                      'SELECT id, source, target, length as cost FROM road_topology_edges_connected'
                  ));

--TODO add bridge to seperate table solve bridge add distance to remaining edges
