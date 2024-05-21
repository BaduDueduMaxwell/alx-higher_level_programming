-- This script prints the full description of the table first_table
-- from the databse hbtn_0c_0 in MySQL server
SELECT TABLE_NAME, TABLE_SCHEMA, CREATE_TABLE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table'
