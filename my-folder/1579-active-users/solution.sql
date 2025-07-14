
-- login >= 5 consecutive days

WITH 
    logins_distinct AS (
        SELECT DISTINCT * FROM logins
    ),
    logins_grp AS (
        SELECT
            *,
            (login_date - 
            INTERVAL '1 day' * (ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date) - 1)
            ) AS grp
        FROM logins_distinct
        ORDER BY id
    ),
    logins_atleast_5_times AS (
        SELECT id
        FROM logins_grp
        GROUP BY grp, id
        HAVING COUNT(*) >= 5
    )

SELECT DISTINCT a.id, a.name
FROM logins_atleast_5_times l
LEFT JOIN accounts a
    ON l.id = a.id
ORDER BY id

-- select * from logins_grp


