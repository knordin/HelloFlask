-- dropping appdb user
drop user appdb cascade;

-- creating appdb...

-- creating tablespace
CREATE TABLESPACE APPDB DATAFILE 'appdb.dbf' SIZE 1G reuse AUTOEXTEND ON nologging;

-- creating user
CREATE USER appdb IDENTIFIED BY kristaalthea
	DEFAULT TABLESPACE APPDB
	QUOTA UNLIMITED ON APPDB;

-- assiging privileges
grant dba to appdb;
grant ALTER ANY PROCEDURE to appdb;
grant ALTER SYSTEM to appdb;
grant CREATE ANY PROCEDURE to appdb;
grant CREATE PROCEDURE to appdb;
grant CREATE TABLE to appdb;
grant DEBUG ANY PROCEDURE to appdb;
grant DEBUG CONNECT SESSION to appdb;
grant EXECUTE ANY PROCEDURE to appdb;
grant UNLIMITED TABLESPACE to appdb;

-- Creates the user table with three columns; user id number, username and password
CREATE TABLE "APPDB"."user" 
   (	"USER_ID" NUMBER(*,0) NOT NULL ENABLE, 
	"USERNAME" VARCHAR2(50 CHAR) NOT NULL ENABLE, 
	"PASSWORD" VARCHAR2(50 CHAR) NOT NULL ENABLE, 
	 PRIMARY KEY ("USER_ID")
   );

-- Creates the USER_PROFILE table with two columns; comment id number and their profile stored as JSON
CREATE TABLE "APPDB"."USER_PROFILE" 
   (	"COMMENT_ID" NUMBER(*,0) NOT NULL ENABLE, 
	"DOC" CLOB, 
	 CONSTRAINT "ENSURE_JSON" CHECK (DOC IS JSON) ENABLE, 
	 PRIMARY KEY ("COMMENT_ID")
   );

-- Creates a JSON Search Index
CREATE INDEX po_search_idx ON user_profile (doc)
INDEXTYPE IS CTXSYS.CONTEXT
PARAMETERS ('section group CTXSYS.JSON_SECTION_GROUP SYNC (ON COMMIT)');

-- How to add in users
truncate table "user";
insert into "user" (user_id, username, password) values (1, 'john', 'doe');
insert into "user" (user_id, username, password) values (2, 'jane', 'doe');
commit;

-- How to add a profile for a user
truncate table user_profile;
insert into user_profile (comment_id, doc) values (1, '{"Profname":"john", "username":"john", "age":22}'); 
insert into user_profile (comment_id, doc) values (2, '{"Profname":"jane", "username":"jane", "age":23}'); 
commit;
