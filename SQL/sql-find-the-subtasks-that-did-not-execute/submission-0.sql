-- Write your query below

-- we need to generate the records that demonstrate 1 3
-- as 1 1, 1 2, 1 3

WITH RECURSIVE subtask_number AS (

    SELECT
    task_id,
    1 as subtask_start, -- this is the anchor part ( like starting point)
    subtasks_count
    from tasks 
    UNION ALL

    SELECT 
    task_id,
    subtask_start+1,
    subtasks_count
    from subtask_number
    where subtask_start < subtasks_count
)
select
s.task_id,s.subtask_start as subtask_id
from subtask_number s 
LEFT JOIN executed e on e.task_id = s.task_id and e.subtask_id = s.subtask_start
where e.task_id is NULL