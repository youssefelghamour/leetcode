/*
  This query calculates the average processing time for each machine between two activities

  1. a1 and a2 are both from the same table, Activity:
     - a1 is used for the first activity (start)
     - a2 is used for the second activity (end)
     - Outcome: The Activity table is split into two parts, one for 'start' activities (a1) and one for 'end' activities (a2)

  2. JOIN:
     - Combines rows from a1 and a2 having the same process_id and machine_id
     - This ensures we're comparing the correct 'start' and 'end' activities for the same process and machine

  3. WHERE:
     - Filters to only include rows where a1 and a2 are different activities (like 'start' and 'end').
     - Outcome: For machine 0, the remaining rows are:
       +------------+------------+---------------+-----------+     +------------+------------+---------------+-----------+
       | machine_id | process_id | activity_type | timestamp |     | machine_id | process_id | activity_type | timestamp |
       +------------+------------+---------------+-----------+     +------------+------------+---------------+-----------+
       | 0          | 0          | start         | 0.712     |     | 0          | 0          | end           | 1.520     |
       | 0          | 1          | start         | 3.140     |     | 0          | 1          | end           | 4.120     |
       +------------+------------+---------------+-----------+     +------------+------------+---------------+-----------+

  4. SELECT:
     - Selects the machine_id from a1.
     - Calculates the average time between the 'start' and 'end'
     - Outcome: For machine 0: ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894

  5. GROUP BY: Groups the results by machine_id to calculate the average processing time for each machine
       +------------+-----------------+
       | machine_id | processing_time |
       +------------+-----------------+
       | 0          | 0.894           |
       +------------+-----------------+
*/
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity AS a1
JOIN Activity AS a2
ON a1.process_id = a2.process_id AND a1.machine_id = a2.machine_id
WHERE a1.activity_type = 'start' AND a2.activity_type = 'end'
GROUP BY a1.machine_id;