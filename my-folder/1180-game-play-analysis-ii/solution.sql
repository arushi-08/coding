# Write your MySQL query statement below


select player_id, device_id
from (select player_id, 
device_id, 
row_number() over(partition by player_id order by event_date) as rn
from activity) as t
where rn = 1
