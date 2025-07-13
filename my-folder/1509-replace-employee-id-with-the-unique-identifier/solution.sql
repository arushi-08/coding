-- Write your PostgreSQL query statement below

-- show unique id of each user, if user doesn have u id replace with null

SELECT
    unique_id,
    name
FROM employees e
LEFT JOIN employeeuni eu
    ON e.id = eu.id

