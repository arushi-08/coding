-- num cancel / total num requests 

WITH unbanned as (
    SELECT *
    FROM users
    WHERE banned = 'No'
),
bound_trips as (
    SELECT *
    FROM trips
    WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
)


SELECT
    request_at as "Day",
    round((1.0*count(case when status<>'completed' then 1 end)/ count(*)) , 2) as "Cancellation Rate"
FROM bound_trips t
JOIN unbanned u
    ON t.client_id = u.users_id
JOIN unbanned d
    ON t.driver_id = d.users_id
GROUP BY request_at

