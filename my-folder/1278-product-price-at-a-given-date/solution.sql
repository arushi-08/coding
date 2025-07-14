


WITH products_filtered AS (
    SELECT *
    FROM products
    WHERE change_date <= '2019-08-16'
),

products_filtered_idx AS (
    SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC ) AS rn
    FROM products_filtered
)

(SELECT
    product_id,
    new_price as price
FROM products_filtered_idx
WHERE rn = 1)
UNION
(SELECT product_id, 10 as price
FROM products 
WHERE product_id not in (SELECT product_id from products_filtered))
