-- This script displays the top 3 cities' temperature during July and Augest ordered by temperature in descending order

USE hbtn_0c_0;

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
