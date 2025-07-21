-- Write your PostgreSQL query statement below


-- user name who rated most num movies, order by num movies, user name
-- movie name with highest avg rating in feb 2020. order by rating, movie name
(
SELECT
    u.name AS results
FROM users u
JOIN movierating mr
    ON u.user_id = mr.user_id
GROUP BY u.user_id, u.name
ORDER BY COUNT(*) DESC, u.name
LIMIT 1)

UNION ALL

(SELECT
    m.title AS results
FROM movies m
JOIN movierating mr
    ON m.movie_id = mr.movie_id
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY m.movie_id, m.title
ORDER BY AVG(rating) DESC, m.title
LIMIT 1)
