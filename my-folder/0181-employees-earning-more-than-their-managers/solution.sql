-- Write your PostgreSQL query statement below

-- emp earning > manager

SELECT
    e.name as employee
FROM employee e
JOIN employee m
    ON e.managerid = m.id
    AND e.salary > m.salary
