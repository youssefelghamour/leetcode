/*
    SELECT departmentId, name, salary,
        DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY salary DESC) AS ranking
    FROM Employee;

        The subquery creates a rank using DENSE_RANK() (to not skip duplicates)
        based on the DESC order of the salaries, in the departmentId window

        Meaning that for each department it ranks tha salaries inside that department

        | departmentId | name  | salary | ranking |
        | ------------ | ----- | ------ | ------- |
        | 1            | Max   | 90000  | 1       |
        | 1            | Joe   | 85000  | 2       |
        | 1            | Randy | 85000  | 2       | accounts for duplicates
        | 1            | Will  | 70000  | 3       | even when there are duplicates, it doesn't skip 3rd place
        | 1            | Janet | 69000  | 4       |
        | 2            | Henry | 80000  | 1       | starts new ranking for the salaries in the 2nd dep
        | 2            | Sam   | 60000  | 2       |
    
    The WHERE e.ranking <= 3 condition would then keep only the top 3 salaries
*/
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
        SELECT departmentId, name, salary,
            DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY salary DESC) AS ranking
        FROM Employee
    ) AS e
JOIN Department d
    ON d.id = e.departmentId
WHERE e.ranking <= 3
;