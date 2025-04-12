/*
  1. DATE_FORMAT(trans_date, '%Y-%m') AS month: 
     Extracts the month in 'YYYY-MM' format from trans_date

  2. COUNT(*) AS trans_count:
     Counts the total number of transactions for each month and country

  3. SUM(state = 'approved') AS approved_count: Counts the number of approved transactions
     - state = 'approved' returns 1 for true and 0 for false, and SUM adds them up

  4. SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END): Sums the amount for approved transactions only
     - The CASE statement checks if the state is 'approved', returning the transaction amount if true, or 0 if false
     - SUM adds up only the amounts where state = 'approved', & ignores rows where the state is not approved (0)
*/
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE
            WHEN state = 'approved'
            THEN amount
            ELSE 0
        END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;