-- Write your PostgreSQL query statement below

WITH RECURSIVE hierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        h.manager_id,
        h.level + 1 AS level
    FROM employees e
    JOIN hierarchy h
        ON e.manager_id = h.employee_id
),
ManagerSubordinates AS (
    -- anchor: each manager to immediate subordinate
    SELECT 
        manager_id,
        employee_id AS subordinate_id,
        salary
    FROM employees
    WHERE manager_id IS NOT NULL

    UNION ALL

    -- recursively fetch subordinates of subordinates
    SELECT 
        ms.manager_id,
        e.employee_id,
        e.salary
    FROM ManagerSubordinates ms
    JOIN employees e ON e.manager_id = ms.subordinate_id
),
-- select * from ManagerSubordinates
team_size_data AS (
    SELECT
        manager_id,
        COUNT(*) AS team_size,
        SUM(salary) AS budget
    FROM ManagerSubordinates
    GROUP BY manager_id
)

-- select * from team_size_data

SELECT  
    e.employee_id,
    e.employee_name,
    h.level,
    COALESCE(ts.team_size, 0) AS team_size,
    COALESCE(ts.budget, 0) + e.salary AS budget
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id
LEFT JOIN hierarchy h
    ON e.employee_id = h.employee_id
LEFT JOIN team_size_data ts
    ON e.employee_id = ts.manager_id
ORDER BY level, budget DESC, e.employee_name
