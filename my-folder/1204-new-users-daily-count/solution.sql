-- Write your PostgreSQL query statement below
With traffic_idx AS (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY activity_date) AS rn
    FROM traffic
    WHERE activity = 'login'
)
-- select * from traffic_idx

SELECT
    activity_date AS login_date,
    COUNT(*) AS user_count
FROM traffic_idx
WHERE rn = 1 AND '2019-06-30' - activity_date <= 90
GROUP BY activity_date
ORDER BY login_date
