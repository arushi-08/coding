-- Write your PostgreSQL query statement below


-- find all aithors that viewed >= 1 own articles

SELECT DISTINCT
    author_id AS id
FROM views 
WHERE author_id = viewer_id
ORDER BY author_id
