# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id + 1
JOIN Logs l3 ON l1.id = l3.id + 2
WHERE l1.num = l2.num AND l1.num = l3.num;

/*
SELECT DICTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.id = l2.id - 1 AND l2.id = l3.id - 1
    AND l1.num = l2.num AND l2.num = l3.num;
*/

/*
# Using LEAD: gets the next row based on the order given to it inside OVER
# OVER(ORDER BY id): Tells it to get the next row based on the order of the ids, so if we're on id 1 go to id 2
# The subquery makes a table containing the num and the two consecutive nums after it
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
        LEAD(num, 1) OVER (ORDER BY id) AS n1,
        LEAD(num, 2) OVER (ORDER BY id) AS n2
    FROM Logs
) t
WHERE num = n1 AND num = n2;
*/