# Write your MySQL query statement below

with nyc as (
    select 'New York University' as uni, count(*) as count 
    from NewYork
    where score >= 90
    ),
cali as (
    select 'California University' as uni, count(*) as count 
    from California
    where score >= 90
)


select (case 
when (select count from nyc) > (select count from cali) then 'New York University'
when (select count from nyc) < (select count from cali) then 'California University'
else 'No Winner' end) as winner
