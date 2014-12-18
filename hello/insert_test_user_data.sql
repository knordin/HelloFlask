truncate table "user";
insert into "user" (user_id, username, password) values (1, 'john', 'doe');
insert into "user" (user_id, username, password) values (2, 'jane', 'doe');
commit;

truncate table user_profile;
insert into user_profile (comment_id, doc) values (1, '{"Profname":"john", "username":"john", "age":22}'); 
insert into user_profile (comment_id, doc) values (2, '{"Profname":"jane", "username":"jane", "age":23}'); 
commit;

/* insert a third user example */

insert into "user" (user_id, username, password) values (3, 'jack', 'doe');
insert into user_profile (comment_id, doc) values (3, '{"Profname":"Jack Doe", "username":"jack", "age":27}');
commit;