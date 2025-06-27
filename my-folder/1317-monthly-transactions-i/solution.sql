# Write your MySQL query statement below

-- find for each month and country, total num of transactions and their total amount
-- num of approved transaction, and total amount


select date_format(trans_date, '%Y-%m') as month, country, count(*) as trans_count, sum(amount) as trans_total_amount, 
sum(if(state='approved', 1, 0)) as approved_count,
sum(if(state='approved', amount, 0)) as approved_total_amount
    from transactions
    group by country, date_format(trans_date, '%Y-%m')

