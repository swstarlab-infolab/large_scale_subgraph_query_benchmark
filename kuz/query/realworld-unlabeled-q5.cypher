MATCH (v0:V0)-[:E0]->(v1:V0)-[:E0]->(v2:V0)-[:E0]->(v3:V0)-[:E0]->(v0)
WHERE NOT (v0)-[:E0]->(v2)
  AND Id(v0) <> Id(v2)
  AND Id(v1) <> Id(v3)
RETURN count(*) AS count
