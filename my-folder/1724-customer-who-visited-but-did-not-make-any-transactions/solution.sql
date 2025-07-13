-- Write your PostgreSQL query statement below

-- find ids of users who visited without any trans
-- number of times they visited

WITH customer_counts AS (
    SELECT
        customer_id
    FROM visits v
    LEFT JOIN transactions t
        ON v.visit_id = t.visit_id
    GROUP BY v.visit_id, v.customer_id
    HAVING sum(amount) IS NULL
)

SELECT
    customer_id,
    COUNT(*) as count_no_trans
FROM customer_counts
GROUP BY customer_id
