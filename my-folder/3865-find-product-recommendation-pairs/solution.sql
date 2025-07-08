-- Write your PostgreSQL query statement below



-- amazon wants to implement customers who bought this also bought
-- distinct product pairs
-- how many custs purchased both

-- if atleast 3 diff custs purchased the pair

-- order by cust_count desc, product1_id, product2_id

with prod_pairs_id as (select pp1.product_id as product1_id, pp2.product_id as product2_id, count(*) as customer_count
from ProductPurchases pp1 join ProductPurchases pp2
on pp1.user_id = pp2.user_id and pp1.product_id < pp2.product_id
group by 1,2
having count(*) > 2
order by customer_count desc, product1_id, product2_id)

select product1_id, product2_id, pi1.category as product1_category, pi2.category as product2_category, customer_count
from prod_pairs_id pp join productinfo pi1
on pp.product1_id = pi1.product_id
join productinfo pi2
on pp.product2_id = pi2.product_id

