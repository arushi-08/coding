-- Write your PostgreSQL query statement below


-- factory has machines
-- each with same processes
-- find avg time each machine takes

-- sum(end - start) / count(processes) group by machine

WITH starttime AS (
    SELECT
        machine_id,
        process_id,
        timestamp as start_time
    FROM activity
    WHERE activity_type = 'start'
),
endtime AS (
    SELECT
        machine_id,
        process_id,
        timestamp as end_time
    FROM activity
    WHERE activity_type = 'end'
)

SELECT
    s.machine_id,
    round((SUM(end_time - start_time)::numeric/ count(*)), 3) AS processing_time
FROM  starttime s
JOIN endtime e
    ON s.machine_id = e.machine_id
    AND s.process_id = e.process_id
GROUP BY s.machine_id
