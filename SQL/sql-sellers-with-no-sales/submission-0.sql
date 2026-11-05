-- Write your query below
select distinct seller_name
from seller s left join orders o 
on o.seller_id = s.seller_id and 
(o.sale_date>'2019-12-31' and o.sale_date<'2021-01-01')
where o.order_id is null
order by seller_name 