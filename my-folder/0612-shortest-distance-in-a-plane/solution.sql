-- Write your MySQL query statement below




-- report shortest dist bet any 2 points from point2d table
-- round(2)

SELECT
    ROUND(POWER(POWER(t1.x - t2.x, 2) + POWER(t1.y - t2.y, 2), 0.5)::numeric, 2) AS shortest
FROM point2d t1
JOIN point2d t2
    ON t1.x <> t2.x OR t1.y <> t2.y
ORDER BY shortest
LIMIT 1

-- SELECT
--     *
-- FROM point2d t1
-- JOIN point2d t2
--     ON t1.x <> t2.x OR t1.y <> t2.y
