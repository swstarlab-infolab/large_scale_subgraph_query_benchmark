CREATE TABLE Continent (
    CompanyId bigint NOT NULL
);

CREATE TABLE Country (
    CountryId bigint NOT NULL
);

CREATE TABLE City (
    CityId bigint NOT NULL
);

CREATE TABLE University (
    UniversityId bigint NOT NULL
);

CREATE TABLE Company (
    CompanyId bigint NOT NULL
);

CREATE TABLE TagClass (
    TagClassId bigint NOT NULL
);

CREATE TABLE Tag (
    TagId bigint NOT NULL
);

CREATE TABLE Forum (
    ForumId bigint NOT NULL
);

CREATE TABLE Person (
    PersonId bigint NOT NULL
);

CREATE TABLE Comment (
    CommentId bigint NOT NULL
);

CREATE TABLE Post (
    PostId bigint NOT NULL
);

CREATE TABLE Comment_hasTag_Tag       (CommentId bigint NOT NULL, TagId        bigint NOT NULL);
CREATE TABLE Post_hasTag_Tag          (PostId    bigint NOT NULL, TagId        bigint NOT NULL);
CREATE TABLE Forum_hasMember_Person   (ForumId   bigint NOT NULL, PersonId     bigint NOT NULL);
CREATE TABLE Forum_hasTag_Tag         (ForumId   bigint NOT NULL, TagId        bigint NOT NULL);
CREATE TABLE Person_hasInterest_Tag   (PersonId  bigint NOT NULL, TagId        bigint NOT NULL);
CREATE TABLE Person_likes_Comment     (PersonId  bigint NOT NULL, CommentId    bigint NOT NULL);
CREATE TABLE Person_likes_Post        (PersonId  bigint NOT NULL, PostId       bigint NOT NULL);
CREATE TABLE Person_studyAt_University(PersonId  bigint NOT NULL, UniversityId bigint NOT NULL);
CREATE TABLE Person_workAt_Company    (PersonId  bigint NOT NULL, CompanyId    bigint NOT NULL);
CREATE TABLE Person_knows_Person      (Person1Id bigint NOT NULL, Person2Id    bigint NOT NULL);

CREATE TABLE City_isPartOf_Country          (CityId        bigint NOT NULL, CountryId   bigint NOT NULL);
CREATE TABLE Country_isPartOf_Continent     (CountryId     bigint NOT NULL, ContinentId bigint NOT NULL);
CREATE TABLE Company_isLocatedIn_Country    (CompanyId     bigint NOT NULL, CountryId   bigint NOT NULL); 
CREATE TABLE University_isLocatedIn_City    (UniversityId  bigint NOT NULL, CityId      bigint NOT NULL); 
CREATE TABLE Comment_isLocatedIn_Country    (CommentId     bigint NOT NULL, CountryId   bigint NOT NULL); 
CREATE TABLE Person_isLocatedIn_City        (PersonId      bigint NOT NULL, CityId      bigint NOT NULL); 
CREATE TABLE Post_isLocatedIn_Country       (PostId        bigint NOT NULL, CountryId   bigint NOT NULL); 
CREATE TABLE TagClass_isSubclassOf_TagClass (TagClass1Id   bigint NOT NULL, TagClass2Id bigint NOT NULL); 
CREATE TABLE Tag_hasType_TagClass           (TagId         bigint NOT NULL, TagClassId  bigint NOT NULL);
CREATE TABLE Forum_containerOf_Post         (ForumId       bigint NOT NULL, PostId      bigint NOT NULL);
CREATE TABLE Forum_hasModerator_Person      (ForumId       bigint NOT NULL, PersonId    bigint NOT NULL);
CREATE TABLE Comment_replyOf_Comment        (Comment1Id    bigint NOT NULL, Comment2Id  bigint NOT NULL);
CREATE TABLE Comment_replyOf_Post           (CommentId     bigint NOT NULL, PostId      bigint NOT NULL);
CREATE TABLE Comment_hasCreator_Person      (CommentId     bigint NOT NULL, PersonId    bigint NOT NULL);
CREATE TABLE Post_hasCreator_Person         (PostId        bigint NOT NULL, PersonId    bigint NOT NULL);
