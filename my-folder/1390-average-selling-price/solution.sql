-- Write your PostgreSQL query statement below


-- avg selling price round(2)
-- no sold -> coalesce(0)

WITH prices_days AS (
    SELECT
    pd.product_id,
    units * price as price,
    units
    FROM prices pd
    LEFT JOIN unitssold u
        ON pd.product_id = u.product_id
        AND pd.start_date <= u.purchase_date AND u.purchase_date <= pd.end_date
)
SELECT
    product_id,
    coalesce(round(SUM(price)::numeric/SUM(units), 2), 0) as average_price
FROM prices_days
GROUP BY product_id
