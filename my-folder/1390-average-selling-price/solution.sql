-- Write your PostgreSQL query statement below

-- find avg = price / units


-- find units in start, end time ( units * price + units * price) / total units

select p.product_id, coalesce(round(sum(price * units)::numeric / sum(units), 2), 0) as average_price
from prices p left join unitssold u
on p.product_id = u.product_id and 
p.start_date <= u.purchase_date and  u.purchase_date <= p.end_date
group by p.product_id
