/*
  1. The subquery (t) calculates the total weight up to each person using their turn (starting from the first person)
  
  2. The WHERE clause keeps only the rows where the total weight is less than 1000
  
  3. Outer query orders the result by the turn in reverse order (starting from the last person)
     to find the last person who got into the bus
  
  4. LIMIT 1 ensures only the last person is selected
*/
SELECT t.person_name
FROM (
        SELECT
            *, 
            SUM(weight) OVER (ORDER BY turn) AS total_weight
        FROM Queue
    ) AS t
WHERE t.total_weight <= 1000
ORDER BY t.turn DESC
LIMIT 1;