MATCH (v0:V0)-[:E0]->(v1:V0)-[:E0]->(v2:V0)-[:E0]->(v3:V0)-[:E0]->(v0)
MATCH (v0)-[:E0]->(v2)
WHERE Id(v1) <> Id(v3)
RETURN count(*) AS count
