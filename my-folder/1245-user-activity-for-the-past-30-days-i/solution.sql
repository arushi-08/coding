# Write your MySQL query statement below


-- find daily active users count for 30 days
-- ending 2019-07-27

select activity_date as day, count(distinct user_id) as active_users
from activity
where datediff('2019-07-27', activity_date) < 30 and datediff('2019-07-27', activity_date) >= 0
group by 1

-- select * from t
