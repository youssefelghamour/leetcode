/*
    - id < (SELECT MAX(id) FROM Seat): If we're not on the last row:
        IF(id % 2 = 0, id - 1, id + 1):
            - If the id is even, substract 1 to make it the id of the prev row
            - If the id is odd, Add 1 to make it the id of the next row
    
    - If we're on the last row:
        IF(id % 2 = 0, id - 1, id):
            - If the id is even, substract 1 to make it the id of the prev row
              (still in a pair with the previous student, so we need to swap them)
            - If the id is odd, that means it's not in a pair, keep the id the same
*/
SELECT
    IF(
        (id < (SELECT MAX(id) FROM Seat)),
        IF(id % 2 = 0, id - 1, id + 1),
        IF(id % 2 = 0, id - 1, id)
    ) AS id,
    student
FROM Seat
ORDER BY id;