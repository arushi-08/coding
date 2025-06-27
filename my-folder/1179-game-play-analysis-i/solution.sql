-- # Write your MySQL query statement below


-- find first login date for each player

select player_id, min(event_date) as first_login
from activity
group by player_id


