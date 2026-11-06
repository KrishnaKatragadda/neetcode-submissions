-- Write your query below
with C as (
select
x,
LAG(x) over(order by x) as prev_x
from point
)
select
min(abs(prev_x - x)) as shortest
from C