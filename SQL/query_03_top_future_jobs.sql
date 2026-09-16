SELECT
    job_title,
    SUM(job_openings) AS demand_growth,
    ROUND(AVG(salary),0) AS avg_salary,
    ROUND(AVG(ai_risk_score),2) AS avg_ai_risk
FROM future_jobs
GROUP BY job_title
ORDER BY demand_growth DESC
LIMIT 10;