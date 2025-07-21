-- Write your PostgreSQL query statement below


-- report sum of all total investment values in 2016
-- same tiv_2015 as 1 + policy holders
-- not located in same city as any other policy holder


WITH count_insurance AS (
    SELECT *,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS count_tiv_2015,
        COUNT(*) OVER(PARTITION BY lat, lon) AS count_lat_lon
    FROM insurance
)

SELECT
    ROUND(SUM(tiv_2016)::numeric, 2) as tiv_2016
FROM count_insurance
WHERE count_tiv_2015 > 1 AND count_lat_lon = 1
