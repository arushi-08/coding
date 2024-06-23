# Write your MySQL query statement below

select product_id, ifnull(round(sum(tprice)/sum(units), 2), 0) as average_price
from (
select p.product_id, ifnull(price * units, 0) as tprice, ifnull(units, 0) as units
from prices as p left join unitssold as u
on p.product_id = u.product_id
where purchase_date >= start_date and purchase_date <= end_date 
or purchase_date is null
) as t
group by product_id

