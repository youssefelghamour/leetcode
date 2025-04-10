/*
  Calculates the average years of experience for employees in each project.

  1. JOIN: the Project table (p) with the Employee table (e) using the employee_id column

  2. SUM and COUNT Calculation:
    - SUM(e.experience_years) calculates the total experience years of all employees for each project
    - COUNT(p.employee_id) counts the number of employees assigned to each project
        (When we group the rows, there will be multiple employee_ids for each project_id, we use count to count them)

  3. AVERAGE:
    - Dividing the total experience years by the number of employees gives the average years of experience per project
    - ROUND(AVG(e.experience_years), 2) AS average_years: We can use AVG:
        - For each group of project_id (formed by the GROUP BY), calculates the avg of the experience_years from e
        - It sums the values in experience_years and divides by the number of rows for that group
        - Same calculation as SUM(experience_years) / COUNT(employee_id)

  4. ROUND:
    - Rounds the result to 2 decimal places.

  5. GROUP BY:
    - Groups the results by project_id, so we get one row per project with the calculated average experience years.
*/
SELECT
    p.project_id,
    ROUND(
        SUM(e.experience_years) / COUNT(p.employee_id), 2
    ) AS average_years
FROM Project p
JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;