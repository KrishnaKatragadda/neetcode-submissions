-- Write your query below

select
-- sum(case
--     when order_date = customer_pref_delivery_date then 1
--     else 0
-- end ) as imm,
-- count(*) as total,
round(100.0* sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(*),2) as immediate_percentage
from delivery