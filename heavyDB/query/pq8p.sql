SELECT count(*)
FROM Message_hasTag_Tag
JOIN Message_replyOf_Message
  ON Message_hasTag_Tag.MessageId = Message_replyOf_Message.Message2Id
JOIN Comment_hasTag_Tag
  ON Message_replyOf_Message.Message1Id = Comment_hasTag_Tag.CommentId
JOIN Comment_hasTag_Tag AS cht2
  ON Message_hasTag_Tag.TagId = cht2.TagId
  AND Message_replyOf_Message.Message1Id = cht2.CommentId
  WHERE Message_hasTag_Tag.TagId != Comment_hasTag_Tag.TagId;
