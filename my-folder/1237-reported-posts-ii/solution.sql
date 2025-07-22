-- Write your PostgreSQL query statement below

-- avg daily % posts that removed after being reported as spam (extra col)
-- round(2)

-- removed + spam / spam

WITH percent_table AS (
    SELECT
        action_date,
        ROUND(100.0*COUNT(DISTINCT r.post_id) / COUNT(DISTINCT a.post_id), 2) as percent
    FROM actions a
    LEFT JOIN removals r
        ON a.post_id = r.post_id
    WHERE extra='spam'
    GROUP BY action_date
)

-- select * from percent_table

SELECT
    ROUND(AVG(percent), 2) AS average_daily_percent
FROM percent_table
