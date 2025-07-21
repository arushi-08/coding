-- Write your PostgreSQL query statement below


-- freq ordre products for each customer
WITH data_cnt AS (
    SELECT
        c.customer_id,
        p.product_id, 
        p.product_name,
        RANK() OVER (PARTITION BY c.customer_id
        ORDER BY COUNT(*) DESC) as rn
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN products p
        ON o.product_id = p.product_id
    GROUP BY c.customer_id, p.product_id, p.product_name
)

-- select * from data_cnt
SELECT
    customer_id,
    product_id, 
    product_name
FROM data_cnt
WHERE rn = 1
