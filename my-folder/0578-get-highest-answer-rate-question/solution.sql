-- Write your PostgreSQL query statement below

-- num times user answered the q by num times user showed q

-- report q that has highest answer rate

SELECT
    question_id AS survey_log
FROM surveylog
GROUP BY question_id
ORDER BY (COUNT(CASE WHEN action='answer' THEN 1 END)*1.0 / COUNT(CASE WHEN action='show' THEN 1 END)) DESC, question_id
LIMIT 1
