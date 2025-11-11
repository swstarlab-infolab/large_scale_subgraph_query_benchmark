MATCH (v0:V0)-[:E1]->(:V1)-[:E7]->(:V2)-[:E13]->(:V3)-[:E15]->(v0)
RETURN count(*) AS count
