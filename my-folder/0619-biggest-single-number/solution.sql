-- Write your PostgreSQL query statement below

(SELECT
    num
FROM mynumbers
GROUP BY num
HAVING COUNT(*) = 1
ORDER BY num DESC)
UNION ALL
(SELECT null)
LIMIT 1

