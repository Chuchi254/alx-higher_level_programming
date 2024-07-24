-- Use the specified database
USE hbtn_0d_usa;

-- Find the state_id for California
SET @state_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1);

-- List all cities of California sorted by cities.id in ascending order
SELECT * FROM cities WHERE state_id = @state_id ORDER BY id ASC;
