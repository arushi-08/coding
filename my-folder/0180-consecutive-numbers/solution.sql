# Write your MySQL query statement below


-- find all nos appear atleast 3 times consecutively

-- select distinct num as ConsecutiveNums
-- from (
--     select row_number() over(partition by num) as rn, rank() over(partition by num) as rnk, num
--     from logs
-- ) as t
-- where rn >= 3 and rnk = 1


-- select row_number() over(partition by num) as rn, rank() over(partition by num order by id) as rnk, num
--     from logs


select distinct l1.num as ConsecutiveNums
from logs l1, logs l2, logs l3
where l1.id = l2.id + 1 and l1.id = l3.id + 2
and l1.num = l2.num and l1.num = l3.num
