-- List the number of records with the same score in the table second_table
-- This script retrieves the score and the count of records from the table second_table, sorted by the count in descending order

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
