-- Write your PostgreSQL query statement below


-- salary < 30000
-- manager left the company
-- 

SELECT DISTINCT
    e.employee_id
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id
WHERE e.manager_id IS NOT NULL AND m.employee_id IS NULL AND e.salary < 30000
ORDER BY e.employee_id
