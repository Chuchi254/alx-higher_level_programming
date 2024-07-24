-- Use the specified database
USE hbtn_0d_usa;

-- List all cities with their corresponding state names
SELECT cities.id, cities.name,
	(SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
