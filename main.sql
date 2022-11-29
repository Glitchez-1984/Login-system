-- Change the database, table, and column names to whatever suits your task and add or remove any values you want
-- Since this creates a new database each time, make sure to run it oncd
CREATE DATABASE sample;
CREATE TABLE sample_table (
    Username varchar(255),
    Password varchar(255)
);
INSERT INTO sample_table(Username, Password)
VALUES ('Frank', '362029');
