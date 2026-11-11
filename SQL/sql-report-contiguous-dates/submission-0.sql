WITH all_dates AS (
    SELECT fail_date AS event_date, 'failed' AS state
    FROM failed
    WHERE fail_date >= '2019-01-01' AND fail_date <= '2019-12-31'
    UNION ALL
    SELECT success_date AS event_date, 'succeeded' AS state
    FROM succeeded
    WHERE success_date >= '2019-01-01' AND success_date <= '2019-12-31'
),
ranked AS (
    SELECT
        event_date,
        state,
        ROW_NUMBER() OVER (ORDER BY event_date) AS rn,
        ROW_NUMBER() OVER (PARTITION BY state ORDER BY event_date) AS state_rn
    FROM all_dates
),
grouped AS (
    SELECT
        event_date,
        state,
        rn - state_rn AS grp
    FROM ranked
)
SELECT
    state AS period_state,
    MIN(event_date) AS start_date,
    MAX(event_date) AS end_date
FROM grouped
GROUP BY state, grp
ORDER BY start_date;
