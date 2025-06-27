-- Write your PostgreSQL query statement below

-- 

with total_sales as (select user_id, product_id, sum(quantity) as tot_qty
from sales as s 
group by user_id, product_id)

select user_id, sum(tot_qty * price) as spending
from total_sales as t left join product as p
on t.product_id = p.product_id
group by user_id
order by spending desc, user_id

