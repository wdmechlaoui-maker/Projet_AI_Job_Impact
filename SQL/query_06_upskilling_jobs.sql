SELECT
    job_role,
    COUNT(*) AS nb_employees,
    SUM(
        CASE
            WHEN upskilling_required = 'Yes' THEN 1
            ELSE 0
        END
    ) AS nb_upskilling,
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN upskilling_required = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS upskilling_rate
FROM ai_job_impact
GROUP BY job_role
ORDER BY upskilling_rate DESC
LIMIT 10;