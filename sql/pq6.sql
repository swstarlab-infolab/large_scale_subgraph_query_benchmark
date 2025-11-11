SELECT count(*)
FROM Person_knows_Person AS PKP1
JOIN Person_knows_Person AS PKP2
  ON PKP1.Person2Id = PKP2.Person1Id
 AND PKP1.Person1Id != PKP2.Person2Id
JOIN Person_hasInterest_Tag
  ON Person_hasInterest_Tag.PersonId = PKP2.Person2Id;