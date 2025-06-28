-- Write your PostgreSQL query statement below

-- order by desc
-- dense_rank()

select score, dense_rank() over(order by score desc) as rank
from scores
