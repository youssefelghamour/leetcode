/*
  Calculates the average selling price for each product

  1. JOIN Prices and UnitsSold on product_id

  2. WHERE: Filters rows where the purchase_date is between the start_date and end_date

  3. SUM and AVERAGE Calculation:
    - SUM(u.units * p.price) calculates total revenue for each product by multiplying units sold with the price (row by row)
    - SUM(u.units) calculates total units sold for each product (group sum)
    - Dividing total revenue by total units gives the average price for that product

  4. IFNULL: If there are no units sold (NULL), it makes the average selling price 0

  5. ROUND: limit the average price to 2 decimal places

  6. GROUP BY: Groups the results by product_id to get one row per product, calculating its average price
*/
SELECT
    p.product_id,
    ROUND(
        IFNULL(
            SUM(u.units * p.price) / SUM(u.units), 0), 2
    ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;