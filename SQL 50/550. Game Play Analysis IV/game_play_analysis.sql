/*
  1. Inner subquery (f) inside the join: gets each player's first login date

  2. Join f with Activity (a): matches players from f and a (same player_id)
    and checks if they logged in on first_login + 1 day
    It keeps players that have a login date one day after their first login

  3. COUNT(*) from the join gives number of players who logged in again the day after their first login

  4. COUNT(DISTINCT player_id) gets the total number of players (doesn't count duplicate player_id)

  5. Final result divides the two counts and rounds the fraction to 2 decimal places
*/
SELECT
    ROUND((
        (   SELECT COUNT(*) AS number_of_second_logins
            FROM Activity a
            JOIN
                (SELECT player_id, MIN(event_date) AS first_login
                FROM Activity
                GROUP BY player_id) f ON a.player_id = f.player_id
            WHERE a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY)
        ) / (
            SELECT COUNT(DISTINCT player_id)
            FROM Activity
        )
    ), 2)
    AS fraction;