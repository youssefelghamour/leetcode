/*
  1. Selects the activity_date from the table

  2. Counts the number of distinct user_id values for each day: number of unique users for that day

  3. Filters the data to only include activities that occurred within the 30 day period ending on '2019-07-27'
     - Uses DATE_SUB to subtract 29 days from '2019-07-27' (30 days including the 27th)
  
  4. Groups the results by activity_date (day) to calculate the active users per day
*/
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY day;