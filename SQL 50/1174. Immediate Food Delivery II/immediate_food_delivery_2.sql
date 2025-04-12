/*
  1. First subquery retrieves the earliest order for each customer by selecting the minimum order_date grouped by customer_id
     This gives the first order placed by each customer

  2. Second subquery counts the "immediate" orders. It compares the earliest order date for each customer with their preferred delivery date
     If they match, the order is considered "immediate," and we count how many first orders are immediate

  3. Third subquery counts the total number of first orders. It uses the same logic from the first subquery but without checking the preferred delivery date
     Simply counting the first orders for all customers

  4. The final calculation divides the count of immediate orders (from step 2) by the total count of first orders (from step 3)
     and multiplies by 100 to get the percentage of immediate first orders among all customers
*/
SELECT
    ROUND((
        (SELECT COUNT(*)  
            FROM 
                (SELECT customer_id, MIN(order_date) AS order_date
                FROM Delivery
                GROUP BY customer_id) AS first_orders  -- [1] Groups by customer and selects the earliest order
            WHERE first_orders.order_date = 
            (SELECT customer_pref_delivery_date 
                FROM Delivery 
                WHERE customer_id = first_orders.customer_id 
                AND order_date = first_orders.order_date)  -- [2] Checks if the first order is immediate
        ) / 
        (SELECT COUNT(*)
        FROM (SELECT customer_id, MIN(order_date) AS order_date
            FROM Delivery
            GROUP BY customer_id) AS first_orders  -- [3] Counts total first orders
        ) * 100), 2
    ) AS immediate_percentage;  -- [4] Calculates the immediate orders percentage