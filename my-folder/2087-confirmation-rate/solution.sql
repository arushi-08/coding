-- Write your PostgreSQL query statement below


-- confirm/ total
-- coalesce(,0)
-- round(2)


SELECT
    s.user_id,
    COALESCE(ROUND(
        1.0*(COUNT(*) FILTER (WHERE action='confirmed'))/COUNT(*), 2
        ), 0) AS confirmation_rate

FROM Signups s
LEFT JOIN confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id
