-- Write your PostgreSQL query statement below


-- find sum of amts for odd and even transactions for each day


SELECT
    transaction_date,
    SUM(CASE WHEN amount & 1 = 1 THEN amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN amount & 1 = 0 THEN amount ELSE 0 END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY 1
