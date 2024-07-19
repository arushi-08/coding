# Write your MySQL query statement below


-- confirmation rate = # confirmed msgs / total # requested confirmation msgs
-- round confirmation rate to 2 decimals
-- find conf rate for each user


-- with t as (select s.user_id, c.action, count(c.time_stamp) as entries
-- from (select user_id from signups) as s left join confirmations as c on s.user_id = c.user_id
-- group by s.user_id, c.action),

-- confirmed as (
--     select user_id, entries
--     from t
--     where action = 'confirmed'
-- ),

-- total as (
--     select distinct user_id, sum(entries) over (partition by user_id) as total
-- from t
-- )
-- -- 

-- -- select s.user_id, c.action, c.time_stamp
-- -- from (select user_id from signups) as s left join confirmations as c on s.user_id = c.user_id

-- -- select * from t
-- -- select * from total

-- select j.user_id as user_id, IFNULL(j.confirmation_rate, 0) as confirmation_rate
-- from(
-- select user_id, round(entries/total, 2) as confirmation_rate
-- from(
-- select t.user_id, IFNULL(t.total, 0) as total, IFNULL(c.entries, 0) as entries
-- from total as t left join confirmed as c on t.user_id = c.user_id
-- ) as p
-- ) as j


select s.user_id, round(avg(if(c.action='confirmed', 1,0)), 2) as confirmation_rate
from (select user_id from signups) as s left join confirmations as c on s.user_id = c.user_id
group by s.user_id
