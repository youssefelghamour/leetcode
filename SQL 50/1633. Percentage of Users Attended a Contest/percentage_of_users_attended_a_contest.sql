/*
  Calculates the percentage of users who have registered for each contest

  1. JOIN: the Register table with the Users table on user_id

  2. COUNT(r.user_id): Counts the number of users registered for each contest (for each contest_id)

  3. SELECT COUNT(user_id) FROM Users: Calculates the total number of users from the Users table

  4. ROUND: 
    - Multiplies by 100 to get the percentage
    - Rounded to two decimal places

  5. GROUP BY: contest_id to get the percentage per contest

  6. ORDER BY:
    - Sorts the results in descending order by percentage
    - In case of ties, it orders by contest_id in ascending order
*/
SELECT
    r.contest_id,
    ROUND(
        (COUNT(r.user_id) / (SELECT COUNT(user_id) FROM Users)) * 100, 2
    ) as percentage
FROM Register r
JOIN Users u
    ON r.user_id = u.user_id 
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;