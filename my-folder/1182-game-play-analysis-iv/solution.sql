# Write your MySQL query statement below



with j as (
    select *
    from(
        select rank() over(partition by player_id order by event_date) as rn, player_id, event_date
        from activity
    ) as t
where rn = 2  
),
k as (
    select player_id, date_add(event_date, INTERVAL 1 DAY) as prev_date
    from activity
)

select round(count(distinct j.player_id)/(select count(distinct player_id) from activity), 2) as fraction
from j left join k on j.event_date = k.prev_date and j.player_id = k.player_id
where k.prev_date is not null and j.rn = 2

