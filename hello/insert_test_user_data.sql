truncate table "user";
insert into "user" (user_id, username, password) values (1, 'john', 'doe');
insert into "user" (user_id, username, password) values (2, 'jane', 'doe');
commit;

truncate table user_profile;
insert into user_profile (comment_id, doc) values (1, '{"Profname":"john", "age":22}'); 
insert into user_profile (comment_id, doc) values (2, '{"Profname":"jane", "age":23}'); 
commit;
