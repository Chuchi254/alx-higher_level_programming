-- Lists all records of the table second_table with a non-null name value from the database hbtn_0c_0
-- This script retrieves the score and name fields from table second_table, excluding rows without a name value, ordered by score in descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
