MATCH (v0:V0)-[:E0]->(v1:V0)-[:E0]->(v2:V0)-[:E0]->(v0)
OPTIONAL MATCH (v2)-[:E0]->(v3:V0)
WHERE Id(v0) <> Id(v3)
  AND Id(v1) <> Id(v3)
RETURN count(*) AS count

