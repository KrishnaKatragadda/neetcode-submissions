-- Write your query below
with cte as(
select 
transaction_id,
rank() over(partition by cast(t.day as date) order by amount desc) as rn
from transactions as t 
)
select  transaction_id from cte 
where rn =1
order by transaction_id