-- Write your PostgreSQL query statement below


-- 1 task everyday
-- for each cont interval of days 

-- generate series 2019-01-01 to 2019-12-31.
-- join with failed/ success
-- group rows that are same state
-- SCD

WITH total_data AS(
    SELECT 
        'failed' AS period_state,
        fail_date AS date
    FROM failed
    UNION ALL
    SELECT
        'succeeded' AS period_state,
        success_date AS date
    FROM succeeded
),
filered_data AS (
    SELECT *
    FROM total_data
    WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
    ORDER BY date
),
start_end_dates AS (
SELECT
    period_state,
    date,
    (CASE 
        WHEN LAG(period_state) OVER () <> period_state OR LAG(period_state) OVER () IS NULL
        THEN date
    END) AS start_date,
    (CASE 
        WHEN LEAD(period_state) OVER () <> period_state OR LEAD(period_state) OVER () IS NULL
        THEN date
    END) AS end_date
FROM filered_data
),

starts AS (
SELECT
    period_state,
    start_date,
    ROW_NUMBER() over () as rn
FROM start_end_dates
WHERE start_date IS NOT NULL
),
ends AS (
SELECT
    period_state,
    end_date,
    ROW_NUMBER() over () as rn
FROM start_end_dates
WHERE end_date IS NOT NULL
)

SELECT
    s.period_state,
    start_date,
    end_date
FROM starts s
JOIN ends e
    ON s.period_state = e.period_state
    AND s.rn = e.rn
