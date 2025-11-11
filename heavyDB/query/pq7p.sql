SELECT count(*)
FROM Message_hasTag_Tag
JOIN Message_hasCreator_Person
  ON Message_hasTag_Tag.MessageId = Message_hasCreator_Person.MessageId
JOIN Message_replyOf_Message 
  ON Message_replyOf_Message.Message2Id = Message_hasTag_Tag.MessageId
JOIN Person_likes_Message
  ON Person_likes_Message.MessageId = Message_hasTag_Tag.MessageId;
