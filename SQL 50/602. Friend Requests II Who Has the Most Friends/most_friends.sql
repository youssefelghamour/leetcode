/*  FIRST query
    - Create a temporary table accepter_requester combining all requester_id and accepter_id
    - Use UNION ALL because a person can be both requester and accepter, and we want to count both
        | id |
        | -- |
        | 1  |
        | 1  |
        | 2  |
        | 3  |
        | 2  |
        | 3  |
        | 3  |
        | 4  |

    SECOND query
    - Group by each person's id
    - Count how many times each id appears (that's be how many friends that id has)
    - Order the result by number of friends in descending order
    - Limit the result to 1 person (the one with the most friends)
*/
WITH accepter_requester AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT id, COUNT(*) AS num
FROM accepter_requester
GROUP BY id
ORDER BY num DESC
LIMIT 1;