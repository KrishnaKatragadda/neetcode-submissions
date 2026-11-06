-- Write your query below

select
T.id,
case
    when T.p_id is null then 'Root'
    when EXISTS(
        select 1 
        from tree p 
        where p.p_id = T.id 
    ) then 'Inner'
    else 'Leaf'
end as type
from tree T -- now you take all these records and perform case