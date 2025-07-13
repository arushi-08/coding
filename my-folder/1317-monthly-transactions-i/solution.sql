-- Write your PostgreSQL query statement below

-- find each month country, num trans

SELECT
    to_char(trans_date, 'YYYY-mm') as month,
    country,
    COALESCE(COUNT(*),0) AS trans_count,
    COALESCE(COUNT(CASE WHEN state='approved' THEN 1 END),0) AS approved_count,
    COALESCE(SUM(amount),0) AS trans_total_amount,
    COALESCE(SUM(CASE WHEN state='approved' THEN amount END),0) AS approved_total_amount
FROM transactions
GROUP BY 2, 1

