-- Write your PostgreSQL query statement below

WITH emp_agg AS (
SELECT
    employee_id
FROM employee
GROUP BY employee_id
HAVING COUNT(*) = 1
)

SELECT
    e2.employee_id,
    e1.department_id
FROM employee e1
JOIN emp_agg e2
ON e1.employee_id = e2.employee_id
UNION
SELECT
    employee_id,
    department_id
FROM employee
WHERE primary_flag = 'Y'
ORDER BY 1

