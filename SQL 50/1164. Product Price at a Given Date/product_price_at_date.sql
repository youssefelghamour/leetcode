-- The subquery gets the latest price for each product_id on or before '2019-08-16'
-- If a product doesn't have a price before that date (NULL), its price will be 10
SELECT 
    DISTINCT p.product_id,
    IFNULL(
        (SELECT new_price 
        FROM Products 
        WHERE product_id = p.product_id 
        AND change_date <= '2019-08-16' 
        ORDER BY change_date DESC 
        LIMIT 1),
        10
    ) AS price
FROM Products p;