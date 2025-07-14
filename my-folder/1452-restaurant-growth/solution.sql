
--  >= 1 customer  daily

-- avg of customer paid in 7 days window current + 6 days before
-- round(2)
-- order by visited on
WITH customer_per_day AS (

    SELECT 
        visited_on, sum(amount) as amount
    FROM customer
    GROUP BY visited_on
),

    rolling_avg AS (
        SELECT
            visited_on,
            SUM(amount) OVER w as amount,
            ROUND(AVG(amount) OVER w , 2) as average_amount,
            ROW_NUMBER() OVER (ORDER BY visited_on) AS rn

        FROM customer_per_day
        WINDOW w AS (ORDER BY visited_on RANGE BETWEEN '6 days' PRECEDING AND CURRENT ROW)
)

SELECT
    visited_on,
    amount,
    average_amount
FROM rolling_avg
WHERE rn >= 7
ORDER BY visited_on
