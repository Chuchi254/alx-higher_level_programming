-- List all records with a score >= 10 in the table second_table from the database hbtn_0c_0
-- This script retrieves fields score and name from the table second_table, displaying records with score >= 10, ordered by score in descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
