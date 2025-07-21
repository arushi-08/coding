-- Write your PostgreSQL query statement below

-- find names of salesp who did not have any orders related to company with name 'red'
WITH salesp_w_red_company AS (
SELECT DISTINCT
    sp.sales_id
FROM salesperson sp
JOIN orders o
    ON sp.sales_id = o.sales_id
JOIN company c
    ON o.com_id = c.com_id
WHERE c.name = 'RED'
)
-- select * from salesp_w_red_company

SELECT DISTINCT
    sp.name
FROM SalesPerson sp
LEFT JOIN salesp_w_red_company sp2
    ON sp.sales_id = sp2.sales_id
WHERE sp2.sales_id IS NULL

