EXPLAIN SELECT count(*)
FROM Message_hasTag_Tag
JOIN Comment_replyOf_Message
  ON Message_hasTag_Tag.MessageId = Comment_replyOf_Message.MessageId
JOIN Comment_hasTag_Tag
  ON Comment_replyOf_Message.CommentId = Comment_hasTag_Tag.CommentId
LEFT JOIN Comment_hasTag_Tag AS cht2
       ON Message_hasTag_Tag.TagId = cht2.TagId
      AND Comment_replyOf_Message.CommentId = cht2.CommentId
    WHERE Message_hasTag_Tag.TagId != Comment_hasTag_Tag.TagId
      AND cht2.TagId IS NULL;
