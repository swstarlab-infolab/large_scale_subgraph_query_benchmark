MATCH (v0:V0)-[:E0]->(v1:V0)-[:E0]->(v2:V0)-[:E0]->(v3:V0)-[:E0]->(v4:V0)-[:E0]->(v0)
MATCH (v0)-[:E0]->(v2)
WHERE Id(v0) <> Id(v3)
  AND Id(v1) <> Id(v3)
  AND Id(v1) <> Id(v4)
  AND Id(v2) <> Id(v4)
RETURN count(*) AS count