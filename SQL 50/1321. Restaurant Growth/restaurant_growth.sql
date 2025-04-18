/*  1. The subquery selects the last day of the first week:
        | DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) |
        | ----------------------------------------- |
        | 2019-01-07                                |

    2. Dates selects all the days after it, so when we count the moving average,
        every day has a week window before it:
        | visited_on |
        | ---------- |
        | 2019-01-07 |
        | 2019-01-08 |
        | 2019-01-09 |
        | 2019-01-10 |

    3. ON DATEDIFF(Dates.visited_on, Customer.visited_on) BETWEEN 0 AND 6
        - for each date in the Dates table, it looks for Customer.visited_on dates that are within a 7-day range:
          from the current date up to 6 days before it
        - meaning that for every date in Dates, it groups 7 previous rows (week) before it from the Csutomer table
        - For example, for visited_on = 2019-01-07, the dates from 2019-01-01 to 2019-01-07 
          will be included in the group to calculate the moving average

    4. SUM(Customer.amount): calculates the total amount spent by customers for each 7 day window
    
    5. ROUND(SUM(Customer.amount) / 7, 2): calculates the moving average amount spent by customers 
      over the 7 days leading up to (and including) the given visited_on date
    
    6. Finally, the query groups the results by Dates.visited_on, which represents the last day of the week
*/
WITH Dates AS (
    SELECT DISTINCT visited_on
    FROM Customer
    WHERE visited_on >= (
        SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
        FROM Customer
    )
)
SELECT
    Dates.visited_on,
    SUM(Customer.amount) AS amount,
    ROUND(SUM(Customer.amount) / 7, 2) AS average_amount
FROM Dates
JOIN Customer
    ON DATEDIFF(Dates.visited_on, Customer.visited_on) BETWEEN 0 AND 6
GROUP BY Dates.visited_on
ORDER BY Dates.visited_on;