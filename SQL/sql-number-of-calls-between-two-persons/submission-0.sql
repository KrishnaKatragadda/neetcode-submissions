-- -- Write your query below
-- with unique_calls as (
--     select 
--     from_id,
--     to_id,
--     duration,
--     row_number() over(partition by from_id,to_id,duration order by duration) as rn
--     from calls 
-- )
-- select
-- from_id as person1,
-- to_id as person2,
-- count(*) as call_count,
-- sum(duration) as total_duration
-- from unique_calls
-- where rn=1 
-- --and from_id<to_id
-- group by from_id,to_id
select
least(from_id, to_id) as person1,
greatest(from_id, to_id) as person2,
count(*) as call_count,
sum(duration) as total_duration
from calls
group by least(from_id,to_id), greatest(from_id, to_id)