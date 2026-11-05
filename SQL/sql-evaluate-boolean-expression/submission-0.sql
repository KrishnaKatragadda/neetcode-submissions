select
e.left_operand,
e.operator,
e.right_operand,
case
when e.operator = '>' and lv.value > rv.value then TRUE
when e.operator = '<' and lv.value < rv.value then TRUE
when e.operator = '=' and lv.value = rv.value then TRUE
else False end as value

from expressions e 
join variables lv on e.left_operand = lv.name
join variables rv on e.right_operand = rv.name