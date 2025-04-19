# Write your MySQL query statement below
SELECT p.product_name,
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
    On p.product_id = o.product_id
WHERE MONTH(o.order_date) = 2 AND YEAR(o.order_date) = 2020
GROUP BY p.product_name
HAVING unit >= 100;