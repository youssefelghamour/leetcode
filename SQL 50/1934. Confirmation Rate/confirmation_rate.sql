/*
  This query calculates the confirmation rate for each user

  1. LEFT JOIN:
    - Joins the Signups table (s) with the Confirmations table (c) on user_id
    - Ensures all users from Signups are included, even those without confirmation actions

  2. SUM(c.action = 'confirmed'):
    - Sums the cases where the action is 'confirmed', counting how many confirmations a user has

  3. COUNT(c.user_id):
    - Counts the total number of actions (both 'confirmed' and 'timeout') for each user

  4. IFNULL(..., 0):
    - Ensures users with no confirmation actions (null values) will have a confirmation rate of 0

  5. ROUND(..., 2):
    - Rounds the confirmation rate to two decimal places

  6. GROUP BY:
    - Groups results by user_id to calculate the confirmation rate for each user
*/
SELECT
    s.user_id,
    ROUND(IFNULL(SUM(c.action = 'confirmed') / COUNT(c.user_id), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY user_id;