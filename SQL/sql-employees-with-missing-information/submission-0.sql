-- Write your query below

-- select e.employee_id
-- from employees e join salaries s
-- on e.employee_id = s.employee_id
-- where e.name is null and s.salary is null
-- order by employee_id

-- select employee_id 
-- from employees 
-- where name is null
-- --order by employee_id
-- union 
-- select employee_id
-- from salaries
-- where salary is null
-- order by employee_id
select coalesce(e.employee_id, s.employee_id) as employee_id
from employees e FULL OUTER JOIN salaries s 
on e.employee_id = s.employee_id
where e.employee_id is NULL or s.employee_id is NULL
order by employee_id