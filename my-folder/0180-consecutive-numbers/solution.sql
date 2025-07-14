
-- 3 times



WITH logs_idx AS (
    SELECT *,
    (id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id ))::integer as grp
    FROM logs
    ORDER BY id
)

SELECT DISTINCT
    num AS ConsecutiveNums
FROM logs_idx
GROUP BY grp, num
HAVING COUNT(*) >= 3

-- select * from logs_idx/
