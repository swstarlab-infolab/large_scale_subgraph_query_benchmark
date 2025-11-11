SELECT count(*)
FROM Person_knows_Person
JOIN Comment_hasCreator_Person
  ON Person_knows_Person.Person1Id = Comment_hasCreator_Person.PersonId
JOIN Comment_replyOf_Post
  ON Comment_hasCreator_Person.CommentId = Comment_replyOf_Post.CommentId
JOIN Post_hasCreator_Person
  ON Person_knows_Person.Person2Id = Post_hasCreator_Person.PersonId 
  AND Post_hasCreator_Person.PostId = Comment_replyOf_Post.PostId
