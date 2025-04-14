/*
  1. Subquery (Product_first_year): 
     - This subquery finds the earliest year (MIN(year)) for each product_id
     - The result is a table with product_id and the first year for each product

  2. Main query: 
     - We select the product_id, year, quantity, and price from the Sales table
     - We join the Sales table with the Product_first_year subquery on the product_id
     
  3. Join condition:
     - We match the product_id from both tables
     - We also ensure that the year in the Sales table matches the first year from the subquery (first_year)
     
  We need a table that only has the product_id and the first year for the sale,
  join it with the normal table insuring the quantity and price correspond to the year selected
  otherwise they could be random because of the grouping and belongs to a diff year from the same product
*/
SELECT Sales.product_id, year AS first_year, quantity, price
FROM Sales
JOIN
    (SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id) AS Product_first_year
ON
    Sales.product_id = Product_first_year.product_id
    AND
    Sales.year = Product_first_year.first_year;