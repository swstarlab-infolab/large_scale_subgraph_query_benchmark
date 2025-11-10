SELECT count(*)
FROM Message_hasTag_Tag
JOIN Comment_replyOf_Message
  ON Message_hasTag_Tag.MessageId = Comment_replyOf_Message.MessageId
JOIN Comment_hasTag_Tag
  ON Comment_replyOf_Message.CommentId = Comment_hasTag_Tag.CommentId
WHERE Message_hasTag_Tag.TagId != Comment_hasTag_Tag.TagId;

