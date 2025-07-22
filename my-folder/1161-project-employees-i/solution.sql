-- Write your PostgreSQL query statement below


-- avg exp years of all emp for each project
-- round(2)

SELECT
    project_id,
    ROUND(AVG(experience_years), 2) AS average_years
FROM project p
JOIN employee e
    ON p.employee_id = e.employee_id
GROUP BY project_id

