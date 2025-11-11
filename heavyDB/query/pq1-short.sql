SELECT count(*)
FROM Forum_hasMember_Person
JOIN Forum_containerOf_Post
  ON Forum_hasMember_Person.ForumId = Forum_containerOf_Post.ForumId
JOIN Comment_replyOf_Post
  ON Forum_containerOf_Post.PostId = Comment_replyOf_Post.PostId
JOIN Comment_hasTag_Tag
  ON Comment_replyOf_Post.CommentId = Comment_hasTag_Tag.CommentId;