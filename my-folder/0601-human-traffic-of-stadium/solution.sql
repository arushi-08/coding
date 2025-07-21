-- Write your PostgreSQL query statement below


-- 3+ consecutive ids and num people >= 100 for each

WITH stadium_w_idx AS (
    SELECT
        *,
        ROW_NUMBER() OVER(ORDER BY visit_date) as rn
    FROM stadium
    WHERE people >= 100
),

grp_data AS (
    SELECT 
    *,
    id - rn AS grp
FROM stadium_w_idx
),
grp_cnt_data AS (
SELECT
    *,
    COUNT(*) OVER (PARTITION BY grp) as grp_count
FROM grp_data)

SELECT
    id,
    visit_date, 
    people
FROM grp_cnt_data
WHERE grp_count >= 3 
