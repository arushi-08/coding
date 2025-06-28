-- Write your PostgreSQL query statement below

-- find people who have the most friends number

-- both gets a friend


select id, count(*) as num
from (select requester_id as id
from RequestAccepted
union all
select accepter_id as id
from RequestAccepted
) as t
group by id
order by count(*) desc
limit 1


