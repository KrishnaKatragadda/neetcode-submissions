-- Write your query below

with cte as (
select
p.product_name, p.product_id, o.order_id,o.order_date,
rank() over(partition by p.product_id order by o.order_date desc) as rn
from orders o join products p
on o.product_id = p.product_id
)
select
product_name, product_id, order_id, order_date
from cte 
where rn = 1
order by product_name asc, product_id asc, order_id asc