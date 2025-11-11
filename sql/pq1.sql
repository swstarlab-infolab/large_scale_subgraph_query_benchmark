SELECT count(*)
FROM City_isPartOf_Country
JOIN Person_isLocatedIn_City
  ON City_isPartOf_Country.CityId = Person_isLocatedIn_City.CityId
JOIN Forum_hasMember_Person
  ON Person_isLocatedIn_City.PersonId = Forum_hasMember_Person.PersonId
JOIN Forum_containerOf_Post
  ON Forum_hasMember_Person.ForumId = Forum_containerOf_Post.ForumId
JOIN Comment_replyOf_Post
  ON Forum_containerOf_Post.PostId = Comment_replyOf_Post.PostId
JOIN Comment_hasTag_Tag
  ON Comment_replyOf_Post.CommentId = Comment_hasTag_Tag.CommentId
JOIN Tag_hasType_TagClass
  ON Comment_hasTag_Tag.TagId = Tag_hasType_TagClass.TagId