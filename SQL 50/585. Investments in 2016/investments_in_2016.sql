# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance i1
WHERE
    i1.tiv_2015 in (
        SELECT i2.tiv_2015
        FROM Insurance i2
        WHERE i2.pid != i1.pid
    )
    AND NOT EXISTS(
        SELECT 1
        FROM Insurance i3
        WHERE i3.pid != i1.pid
            AND i3.lat = i1.lat
            AND i3.lon = i1.lon
    );
/*
(i1.lat, i1.lon) not in (
        SELECT i3.lat, i3.lon
        FROM Insurance i3
        WHERE i3.pid != i1.pid
    )
*/