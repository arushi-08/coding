# Write your MySQL query statement below

-- find price of products on 2019-08-16
-- original 10 


with p1 as (
    select product_id, new_price as price
    from (
        select product_id, new_price, row_number() over( partition by product_id order by
        change_date desc) as rn
        from (
            select product_id, new_price, change_date
            from products
            where change_date <= date('2019-08-16')
        ) as t ) as p
    where rn = 1
)

select * from p1
union
select product_id, 10 as price
from products
where product_id not in (select product_id from p1)

