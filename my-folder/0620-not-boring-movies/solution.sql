-- Write your PostgreSQL query statement below


-- report movies with odd numbered ID & description i.e., not boring


SELECT
    *
FROM cinema
WHERE id % 2 = 1 AND description not like '%boring%'
ORDER BY rating DESC
