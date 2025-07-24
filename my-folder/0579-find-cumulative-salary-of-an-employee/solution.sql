-- Write your PostgreSQL query statement below

-- calculate cum salary summary for every emp in a single unified table
-- for each month that emp worked, sum up salaries in that month and prev 2 
-- 3 month sum
-- if no prev months, then effective slaary is 0


-- order by id, month desc
WITH prev_month_salary AS 
(
    SELECT
        id,
        month,
        LAG(month) OVER w AS prev_month,
        (CASE 
            WHEN LAG(month) OVER w = month - 1
            THEN LAG(salary) OVER w
            ELSE 0
        END) as prev_month_salary,
        salary
    FROM employee
    WINDOW w AS (PARTITION BY id ORDER BY month)
),
prev_prev_month_data AS (
    SELECT
        id,
        month,
        prev_month_salary,
        (CASE 
            WHEN LAG(prev_month) OVER w = month - 2
            THEN LAG(prev_month_salary) OVER w
            ELSE 0
        END) as prev_prev_month_salary,
        salary
    FROM prev_month_salary
    WINDOW w AS (PARTITION BY id ORDER BY month)
),
exclude_rows AS (
SELECT
    id,
    MAX(month) OVER (PARTITION BY id) as max_month
FROM employee
) 

SELECT
    md.id,
    month,
    salary + prev_month_salary + prev_prev_month_salary AS Salary
FROM prev_prev_month_data md
LEFT JOIN exclude_rows er
    ON md.id = er.id
    AND md.month = er.max_month
WHERE er.max_month IS NULL
ORDER BY id, month DESC

