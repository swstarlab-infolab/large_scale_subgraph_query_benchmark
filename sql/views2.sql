-- create a common table for the message nodes and edges starting from/ending in message nodes.
CREATE VIEW Message AS
  SELECT CommentId AS MessageId FROM Comment
  UNION ALL
  SELECT PostId AS MessageId FROM Post;

CREATE VIEW Comment_replyOf_Message AS
  SELECT Comment1Id AS CommentId, Comment2Id AS MessageId FROM Comment_replyOf_Comment
  UNION ALL
  SELECT CommentId, PostId AS MessageId FROM Comment_replyOf_Post;

CREATE VIEW Message_hasCreator_Person AS
  SELECT CommentId AS MessageId, PersonId FROM Comment_hasCreator_Person
  UNION ALL
  SELECT PostId AS MessageId, PersonId FROM Post_hasCreator_Person;

CREATE VIEW Message_hasTag_Tag AS
  SELECT CommentId AS MessageId, TagId FROM Comment_hasTag_Tag
  UNION ALL
  SELECT PostId AS MessageId, TagId FROM Post_hasTag_Tag;
 
CREATE VIEW Message_isLocatedIn_Country AS
  SELECT CommentId AS MessageId, CountryId FROM Comment_isLocatedIn_Country
  UNION ALL
  SELECT PostId AS MessageId, CountryId FROM Post_isLocatedIn_Country;

CREATE VIEW Person_likes_Message AS
  SELECT PersonId, CommentId AS MessageId FROM Person_likes_Comment
  UNION ALL
  SELECT PersonId, PostId AS MessageId FROM Person_likes_Post;
