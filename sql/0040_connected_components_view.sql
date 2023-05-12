CREATE OR REPLACE VIEW connected_components_view AS
SELECT road_topology_nodes.id, a.component, road_topology_nodes.geom
from road_topology_nodes
         left join (SELECT node, component
                    FROM pgr_strongcomponents('Select id,source,target,cost,inverse_cost as reverse_cost from road_topology_edges')) a
                   on road_topology_nodes.id = a.node;

CREATE OR REPLACE VIEW longest_connected_component AS
SELECT component
from connected_components_view
group by component
order by count(*) desc
limit 1;

CREATE OR REPLACE VIEW road_topology_edges_connected AS
SELECT *
from road_topology_edges edges
where source in
      (select id from connected_components_view where component = (select component from longest_connected_component))
  and target in
      (select id from connected_components_view where component = (select component from longest_connected_component));