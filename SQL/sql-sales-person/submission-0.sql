-- Write your query below
select distinct p.name
from company c join orders o 
on c.com_id = o.com_id and c.name ='CRIMSON'
right join sales_person p on p.sales_id = o.sales_id
where o.order_id is null; 