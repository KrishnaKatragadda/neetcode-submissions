-- Write your query below

-- you are trying to compare two recrods in a table,
-- use self join
select
distinct
a.account_id
from log_info a join log_info b
on a.account_id = b.account_id
and a.ip_address <> b.ip_address
and a.login <=b.logout and a.logout>=b.login