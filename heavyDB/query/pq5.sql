SELECT count(*)
FROM Message_hasTag_Tag
JOIN Message_replyOf_Message
  ON Message_hasTag_Tag.MessageId = Message_replyOf_Message.Message2Id
JOIN Comment_hasTag_Tag
  ON Message_replyOf_Message.Message1Id = Comment_hasTag_Tag.CommentId
WHERE Message_hasTag_Tag.TagId != Comment_hasTag_Tag.TagId;

