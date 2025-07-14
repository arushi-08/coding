
WITH user_transactions_yr AS (
    SELECT product_id, sum(spend) as spend, 
    TO_CHAR(transaction_date, 'YYYY') as transaction_date
    FROM user_transactions
    GROUP BY product_id, TO_CHAR(transaction_date, 'YYYY')
)

SELECT
    CAST(transaction_date AS INTEGER) as year,
    product_id,
    spend as curr_year_spend,
    LAG(spend) OVER w AS prev_year_spend,
    ROUND(100.0 * (spend - LAG(spend) OVER w) / LAG(spend) OVER w, 2)AS yoy_rate
FROM user_transactions_yr
WINDOW w AS (PARTITION BY product_id ORDER BY transaction_date)
ORDER BY product_id, transaction_date
