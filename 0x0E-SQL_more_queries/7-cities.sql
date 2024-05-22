-- This script creates the hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
