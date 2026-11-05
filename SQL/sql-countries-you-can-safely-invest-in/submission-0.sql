-- Write your query below
select
c.name as country
from person p
join country c on substring(p.phone_number,1,3)= c.country_code
join calls ca on p.id = caller_id or p.id = callee_id
-- This gives country and assoicated call durations
-- peru, isreal 60
group by c.name
having AVG(ca.duration) > (select avg(duration) from calls)