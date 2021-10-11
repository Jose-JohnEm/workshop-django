create user postgres;
create database postgres;
grant all privileges on database postgres to postgres;
create table user(int id);
create table post(int id);
create table comment(int id);
