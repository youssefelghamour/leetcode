# Write your MySQL query statement below
SELECT max(num) AS num
FROM
    (SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1) AS Single_numbers
;