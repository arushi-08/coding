-- Write your PostgreSQL query statement below


-- num acceptance / requests
-- round(2)
WITH requestaccepted_unique AS (
    SELECT COUNT(DISTINCT
        (requester_id,
        accepter_id)) AS accepted
    FROM requestaccepted
),
friendrequest_unique AS (
    SELECT COUNT(DISTINCT
        (sender_id,
        send_to_id)) AS "sent"
    FROM FriendRequest
)

SELECT
    COALESCE( ROUND( accepted*1.0 / NULLIF("sent", 0) , 2), 0.0) AS accept_rate
FROM requestaccepted_unique, friendrequest_unique

