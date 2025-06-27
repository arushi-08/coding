-- Write your PostgreSQL query statement below


-- calculate common_perms ; the access level granted to all users
-- any_perms

select bit_and(permissions) as common_perms, bit_or(permissions) as any_perms
from user_permissions

