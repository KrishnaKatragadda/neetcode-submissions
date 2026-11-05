-- Write your query below

select
w.name as warehouse_name, sum((units*width*length*height)) as volume
from warehouse w join 
products p on w.product_id = p.product_id
group by w.name