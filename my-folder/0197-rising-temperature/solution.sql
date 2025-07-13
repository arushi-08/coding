-- Write your PostgreSQL query statement below

-- find all dates id with > temps comp to prev dates

WITH data_w_prev_date as (
    SELECT
        *,
        LAG(temperature) OVER(ORDER BY recordDate) as prev_temp,
        LAG(recordDate) OVER(ORDER BY recordDate) as prev_date
    FROM weather
)

SELECT id
FROM data_w_prev_date
WHERE temperature > prev_temp
AND recordDate - 1 = prev_date
