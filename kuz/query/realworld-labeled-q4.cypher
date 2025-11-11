MATCH (v0:V0)-[:E1]->(:V1)-[:E7]->(v2:V2)-[:E10]->(v0)
OPTIONAL MATCH (v2)-[:E13]->(:V3)
RETURN count(*) AS count
