
-- find num times each student attended each exam 

WITH not_attended AS (
    SELECT student_id, subject_name, 0 as attended
    FROM students s, subjects
    WHERE (s.student_id, subject_name) not in (
        SELECT *
        FROM examinations
    )
),
total_examinations as (
(SELECT *, 1 as attended
FROM examinations)
UNION ALL
(SELECT * FROM not_attended)
)

SELECT
    s.student_id,
    s.student_name,
    e.subject_name,
    COALESCE(SUM(attended),0) as attended_exams
FROM students s 
JOIN total_examinations e
    ON s.student_id = e.student_id

GROUP BY 1, 2, 3
ORDER BY 1

-- SELECT *
-- FROM students s 
-- CROSS JOIN subjects sub
-- LEFT JOIN examinations e
--     ON s.student_id = e.student_id
