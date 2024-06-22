# Write your MySQL query statement below


with s1 as (select product_id, price as store1 from products where store='store1'),
s2 as (select product_id, price as store2 from products where store='store2'),
s3 as (select product_id, price as store3 from products where store='store3')

select distinct p.product_id, s1.store1, s2.store2, s3.store3
from products as p left join s1 
on p.product_id = s1.product_id
left join s2 
on p.product_id = s2.product_id
left join s3
on p.product_id = s3.product_id


