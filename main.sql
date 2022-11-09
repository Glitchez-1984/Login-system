-- Change the database, table, and column names to whatever suits your task and add or remove any values you want
CREATE DATABASE sample;
CREATE TABLE sample_table (
    Username varchar(255),
    Password varchar(255)
);
INSERT INTO sample_table(Username, Password)
VALUES ('bob', 'abc123');
