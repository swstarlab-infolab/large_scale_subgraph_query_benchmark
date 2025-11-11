EXPLAIN MATCH (:Person)<-[:Forum_hasMember_Person]-(:Forum)-[:Forum_containerOf_Message]->(:Message)<-[:Message_replyOf_Message]-(:Message)-[:Message_hasTag_Tag]->(:Tag)
RETURN count(*) AS count
