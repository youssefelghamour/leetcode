# Selects employees belonging to only one department having primary_flag N
SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1

UNION  -- Combine the two tables

# Selects employees belonging to multiple departments BUT only select department with primary_flag Y
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
GROUP BY employee_id;