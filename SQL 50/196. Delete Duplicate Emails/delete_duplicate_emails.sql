# Write your MySQL query statement below
DELETE FROM Person
WHERE id NOT IN ( -- Deletes the rows that are not the actual min id
    SELECT id
    FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
    ) AS temp -- Table containing one row with the smallest id from all rows with duplicate emails
);
/*
    DELETE p1
    FROM person p1
    JOIN person p2
        ON p1.email = p2.email
        AND p1.id > p2.id
*/