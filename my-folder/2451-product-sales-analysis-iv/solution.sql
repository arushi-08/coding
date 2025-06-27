-- Write your PostgreSQL query statement below

-- each user all pid, max(price), 

-- select price * quantity
-- from sales as s left join product as p
-- on s.product_id = p.product_id

with total_sale as (select product_id, user_id, sum(quantity) as total_qty
from sales
group by product_id, user_id)

-- per pid, per user, price, total_qty
select user_id, product_id
from (select user_id, s.product_id as product_id, rank() over (partition by user_id order by price * total_qty desc) as rank
from total_sale as s left join product as p
on s.product_id = p.product_id) as t
where rank = 1

-- select user_id, s.product_id as product_id, price * total_qty, rank() over (partition by user_id order by price * total_qty desc) as rank
-- from total_sale as s left join product as p
-- on s.product_id = p.product_id

