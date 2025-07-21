-- Write your PostgreSQL query statement below


-- calculate each user's avg daily activity duration during free trial period
-- same for paid
-- order by user id

WITH avg_duration AS (
    SELECT
        user_id,
        ROUND(AVG(CASE WHEN activity_type='free_trial' THEN activity_duration END), 2) as trial_avg_duration,
        ROUND(AVG(CASE WHEN activity_type='paid' THEN activity_duration END), 2) as paid_avg_duration
    FROM useractivity
    GROUP BY user_id
)

SELECT *
FROM avg_duration
WHERE paid_avg_duration IS NOT NULL
ORDER BY user_id
