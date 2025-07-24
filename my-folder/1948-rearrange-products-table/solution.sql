-- Write your PostgreSQL query statement below


-- write soln to rearrange products table each row has prod id, store, price
-- if product is not available in store, don't include row with 

SELECT
    product_id,
    'store1' AS store,
    store1 AS price
FROM products
WHERE store1 IS NOT NULL
UNION ALL
SELECT
    product_id,
    'store2' AS store,
    store2 AS price
FROM products
WHERE store2 IS NOT NULL
UNION ALL
SELECT
    product_id,
    'store3' AS store,
    store3 AS price
FROM products
WHERE store3 IS NOT NULL
