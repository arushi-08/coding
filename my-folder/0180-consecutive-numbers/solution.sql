-- Write your PostgreSQL query statement below

-- 

SELECT DISTINCT
    l1.num as ConsecutiveNums
FROM logs l1
JOIN logs l2
    ON l1.id + 1 = l2.id
    AND l1.num = l2.num
JOIN logs l3
    ON l1.id + 2 = l3.id
    AND l2.num = l3.num
