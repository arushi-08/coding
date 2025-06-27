-- Write your PostgreSQL query statement below

-- report buyers who have bought s8 but not iphone
-- 

select distinct buyer_id
from sales
where buyer_id not in ( 
    select distinct buyer_id 
    from sales 
    where product_id in (
        select product_id
        from product
        where product_name = 'iPhone'
        ) 
    )
and product_id in (select product_id from product where product_name = 'S8' )



