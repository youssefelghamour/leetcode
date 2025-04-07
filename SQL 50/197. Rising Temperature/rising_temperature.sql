/*
  This query compares each day's temperature (w1) with the previous day's temperature (w2)
  - w1 is the current row (today's date)
  - w2 is the row from the previous day (earlier date)
  
  The subquery for `w2` does the following:
  - WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY): Keeps only the row from yesterday (id it exists)
  - DATE_SUB(w1.recordDate, INTERVAL 1 DAY): subtracts a specified time interval from a date in this case 1 day
  
  The outer query compares the temperature of `w1` (today) with the temperature of the previous day (`w2`).
*/
SELECT w1.id
FROM Weather AS w1
WHERE w1.temperature > (
    SELECT w2.temperature
    FROM Weather AS w2
    WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
);

/*
  We are performing a self join on the Weather table
  - w1 represents the current day (today)
  - w2 represents the previous day (yesterday)
  The goal is to join each row in w1 (today) with the corresponding row in w2 (yesterday)
  
  The condition "w1.recordDate = w2.recordDate + INTERVAL 1 DAY" ensures that:
  - w1's date is exactly one day ahead of w2's date (matching today to yesterday)
*/
-- SELECT w1.id
-- FROM Weather w1
-- JOIN Weather w2
-- ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
-- WHERE w1.temperature > w2.temperature;