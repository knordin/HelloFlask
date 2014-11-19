prompt >> Dropping appdb user
drop user appdb cascade;
prompt >> Creating appdb...

prompt >> Creating tablespace
CREATE TABLESPACE APPDB DATAFILE 'appdb.dbf' SIZE 1G reuse AUTOEXTEND ON nologging;

prompt >> Creating user
CREATE USER appdb IDENTIFIED BY kristaalthea
	DEFAULT TABLESPACE APPDB
	QUOTA UNLIMITED ON APPDB;

prompt >> Assiging privileges
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


