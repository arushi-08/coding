-- Write your MySQL query statement below

-- books - 
-- orders

-- report books that have sold < 10 copies in last year, excluding books available for less than 1 month from today
-- available_from <= CURRENT_DATE - INTERVAL '1 month'


WITH books_available_gt_1_month AS (
    SELECT *
    FROM books
    WHERE available_from <= DATE '2019-06-23' - INTERVAL '1 month'
),
last_year_orders AS (
    SELECT *
    FROM orders
    WHERE dispatch_date >=  DATE '2019-06-23' - INTERVAL '1 year'
)

-- select * from last_year_orders

SELECT
    b.book_id,
    "name"
    -- SUM(quantity) 
FROM books_available_gt_1_month b
LEFT JOIN last_year_orders o
    ON b.book_id = o.book_id
GROUP BY b.book_id, "name"
HAVING SUM(COALESCE(quantity, 0)) < 10
