/*
  1. ROUND(AVG(rating / position), 2): the average of the ratio between rating and position for each query

  2. ROUND(
       ((SELECT COUNT(*) FROM Queries q2 WHERE q2.query_name = q1.query_name AND rating < 3) / COUNT(rating)) * 100, 2
    )
    - Calculates the percentage of queries with rating less than 3 (poor queries)
        - SELECT COUNT(*) counts the number of queries for each query_name with a rating less than 3
        - COUNT(rating) counts the total number of queries for each query_name in the outer query q1
    
    ROUND(100 * SUM(rating < 3) / COUNT(*), 2) AS poor_query_percentage:
        - SUM(rating < 3): Counts how many queries have a rating less than 3
*/
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(
        (
            (SELECT COUNT(*) FROM Queries q2 WHERE q2.query_name = q1.query_name AND rating < 3) / COUNT(rating)
            * 100
        ), 2
    ) AS poor_query_percentage
FROM Queries q1
GROUP BY query_name;