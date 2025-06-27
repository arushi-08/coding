-- Write your PostgreSQL query statement below

-- report total qty sold for every product id
-- sum(quat) for every p id

select product_id, sum(quantity) as total_quantity
from sales
group by product_id
