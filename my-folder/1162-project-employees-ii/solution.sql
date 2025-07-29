# Write your MySQL query statement below


-- report all projects that have most emps


SELECT project_id
FROM project
GROUP BY project_id
HAVING COUNT(*) = (
    SELECT MAX(max_count)
    FROM (SELECT COUNT(*) AS max_count
    FROM project
    GROUP BY project_id) t
)
