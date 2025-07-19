-- Write your PostgreSQL query statement below


-- report sum of all total investment values in 2016
-- same tiv_2015 as 1 + policy holders
-- not located in same city as any other policy holder

WITH unique_locations AS(
    SELECT lat, lon
    FROM insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1 
),

same_tiv_2015 AS (
    SELECT tiv_2015
    FROM insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)

SELECT
    ROUND(SUM(i.tiv_2016)::numeric, 2) as tiv_2016
FROM insurance i
JOIN unique_locations l
ON i.lat = l.lat AND i.lon = l.lon
JOIN same_tiv_2015 t
ON i.tiv_2015 = t.tiv_2015

