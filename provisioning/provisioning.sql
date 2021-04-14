CREATE KEYSPACE test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
USE test;
CREATE TABLE employee (
   employ_id text PRIMARY KEY,
   name text,
   description text
);
INSERT INTO employee (employ_id, name, description )
VALUES ( 'BR1', 'Momotaro', 'A good boy');
INSERT INTO employee (employ_id, name, description )
VALUES ( 'BR2', 'Momotato', 'A good girl');
