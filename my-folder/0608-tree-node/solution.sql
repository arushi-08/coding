-- Write your PostgreSQL query statement below

SELECT DISTINCT
    c.id,
    (CASE 
        WHEN c.p_id IS NULL
        THEN 'Root'
        WHEN child.id IS NULL
        THEN 'Leaf'
        ELSE 'Inner'
    END) AS type

FROM tree c
LEFT JOIN tree p
    ON c.p_id = p.id
LEFT JOIN tree child
    ON c.id = child.p_id
ORDER BY c.id

-- SELECT
--     *
-- FROM tree c
-- LEFT JOIN tree p
--     ON c.p_id = p.id
-- LEFT JOIN tree child
--     ON c.id = child.p_id
-- ORDER BY c.id
