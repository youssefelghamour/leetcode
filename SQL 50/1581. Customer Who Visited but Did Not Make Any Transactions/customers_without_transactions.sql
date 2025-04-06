# Gets the customer_id from the Visits table where there is no matching visit_id in the Transactions table
# LEFT JOIN: Keeps all visits, even those without a matching transaction
# WHERE Transactions.visit_id IS NULL: Filters out visits that have a matching transaction
# COUNT(Visits.visit_id): Counts visits for each customer
# GROUP BY Visits.customer_id: Groups rows having the same customer_id then counts the occurence (number of rows in each group)
SELECT Visits.customer_id, COUNT(Visits.visit_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id IS NULL
GROUP BY Visits.customer_id;