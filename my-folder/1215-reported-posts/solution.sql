-- Write your PostgreSQL query statement below

-- report num of posts reported yesst for each report reason
-- 2019-07-05

SELECT
    extra AS report_reason,
    COUNT(DISTINCT post_id) AS report_count
FROM actions
WHERE action = 'report' AND action_date = DATE '2019-07-04'
GROUP BY extra

