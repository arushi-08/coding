-- Write your PostgreSQL query statement below


-- name of prods 100+ units ordered in feb 2020

SELECT
    product_name,
    SUM(unit) as unit
FROM products p
JOIN orders o
    ON p.product_id = o.product_id
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY o.product_id, product_name
HAVING SUM(unit) >= 100
