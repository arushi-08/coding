-- Write your PostgreSQL query statement below

-- % users registered in each contest round(2)
-- order by percentage desc, contest id
WITH total_users AS (
    SELECT COUNT(DISTINCT user_id) AS total_users_count
    FROM users
)

SELECT
    contest_id,
    ROUND(100.0*COUNT(DISTINCT user_id) / total_users_count,2) AS percentage
FROM register, total_users
GROUP BY contest_id, total_users_count
ORDER BY percentage DESC, contest_id
