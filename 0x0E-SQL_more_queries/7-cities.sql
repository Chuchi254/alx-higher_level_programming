-- Create the database hbtn_0d_usa if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states if not exists (necessary for foreign key constraint)
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);

-- Create the table cities if not exists
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
