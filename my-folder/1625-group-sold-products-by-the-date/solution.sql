
SELECT 
    sell_date,
    COUNT(*) AS num_sold,
    ARRAY_TO_STRING(ARRAY_AGG(product ORDER BY product), ',') AS products
FROM (SELECT DISTINCT * FROM activities) t
GROUP BY sell_date
ORDER BY sell_date
