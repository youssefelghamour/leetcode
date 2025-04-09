/*
  This query finds managers with at least 5 direct reports

  1. SELF JOIN:
    - Joins the Employee table to itself
    - e1 is treated as the manager, e2 as the employee
    - ON e1.id = e2.managerId matches each manager to their direct reports
    - That means e2 is managed by e1

  2. GROUP BY:
    - Groups results by manager id (e1.id)
    - So we count how many employees each manager has

  3. HAVING:
    - Filters only those managers who have 5 or more direct reports
*/
SELECT e1.name
FROM Employee e1
JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(*) >= 5;