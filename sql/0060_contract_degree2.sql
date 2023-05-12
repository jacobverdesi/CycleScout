
CREATE OR REPLACE VIEW degree2Nodes AS
(
SELECT nodes.id,nodes.geom
FROM road_topology_nodes nodes
         Left join road_topology_no_bridge edges on
             nodes.id = edges.source or nodes.id = edges.target
Group by nodes.id,nodes.geom
HAVING count(nodes.id) = 2);

