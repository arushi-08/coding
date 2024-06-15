# Write your MySQL query statement below

-- end time - start time / # processes

with st as (select machine_id, process_id, timestamp
from activity
where activity_type = 'start'),
ed as (select machine_id, process_id, timestamp
from activity
where activity_type = 'end')

select machine_id, round(avg(difference), 3) as processing_time
from(
    select st.machine_id, st.process_id, (ed.timestamp - st.timestamp) as difference
    from st join ed
    on st.machine_id = ed.machine_id and st.process_id = ed.process_id
) as d
group by machine_id
