-- # Write your MySQL query statement below



-- report the most exp employees in each project
-- in case of tie, report all emps with max exp years
WITH data_ranked AS (
SELECT
    project_id,
    p.employee_id,
    experience_years,
    RANK() OVER(PARTITION BY project_id ORDER BY experience_years DESC) AS rn
FROM project p
JOIN employee e
    ON p.employee_id = e.employee_id
)

SELECT
    project_id,
    employee_id
FROM data_ranked
WHERE rn = 1


