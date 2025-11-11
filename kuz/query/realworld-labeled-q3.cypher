MATCH (v0:V0)-[:E1]->(:V1)-[:E7]->(v2:V2)-[:E13]->(:V3)-[:E19]->(:V4)-[:E20]->(v0)
MATCH (v0)-[:E2]->(v2)
RETURN count(*) AS count