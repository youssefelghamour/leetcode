/*
    - ratings_per_user: Get the user with the most ratings:
        -- Table Result for the subquery:
        +-----------+-----------+------------------+
        | user_id   | name      | number_of_ratings|
        +-----------+-----------+------------------+
        | 1         | Daniel    | 3                |
        | 2         | Monica    | 2                |
        | 3         | Maria     | 2                |
        | 4         | James     | 1                |
        +-----------+-----------+------------------+
        
        -- The final result of ratings_per_user after LIMIT 1 is:
        +-----------+-----------+-------------------+
        | user_id   | name      | number_of_ratings |
        +-----------+-----------+-------------------+
        | 1         | Daniel    | 3                 |
        +-----------+-----------+-------------------+
    
    - The final result of the first query is:
        +------------+
        | results    |
        +------------+
        | Daniel     |
        +------------+
    
    - movies_feb_ratings: Get the movie with the highest average rating in February 2020:
        -- Table Result for the subquery before LIMIT 1:
        +----------+--------------+-------------------+
        | movie_id | title        | average_rating    |
        +----------+--------------+-------------------+
        | 2        | Frozen 2     | 3.5               |
        | 3        | Joker        | 3.5               |
        | 1        | Avengers     | 3                 |
        +----------+--------------+-------------------+
        
        -- The final result of movies_feb_ratings after LIMIT 1 is: 
        +----------+--------------+-------------------+
        | movie_id | title        | average_rating    |
        +----------+--------------+-------------------+
        | 2        | Frozen 2     | 3.5               |
        +----------+--------------+-------------------+

    - The final result of the second query is:
        +-----------+
        | results   |
        +-----------+
        | Frozen 2  |
        +-----------+
        
    - UNION ALL: Combine the results from both queries into one final result:
        +------------------+
        | results          |
        +------------------+
        | Daniel           |
        | Frozen 2         |
        +------------------+
*/

SELECT ratings_per_user.name as results
FROM (
        SELECT
            MovieRating.user_id,
            Users.name,
            COUNT(rating) AS number_of_ratings
        FROM MovieRating
        LEFT JOIN Users
            ON MovieRating.user_id = Users.user_id
        GROUP BY MovieRating.user_id
        ORDER BY
            number_of_ratings DESC,
            Users.name
        LIMIT 1
    ) ratings_per_user

UNION ALL

SELECT title as results
FROM (
        SELECT
            mr.movie_id,
            m.title,
            AVG(mr.rating) AS average_rating
        FROM MovieRating AS mr
        LEFT JOIN Movies AS m
            ON mr.movie_id = m.movie_id
        WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
        GROUP BY mr.movie_id
        ORDER BY
            average_rating DESC,
            m.title
        LIMIT 1
    ) movies_feb_ratings
;