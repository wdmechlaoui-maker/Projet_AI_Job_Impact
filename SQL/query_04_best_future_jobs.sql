SELECT
    job_title,
    SUM(job_openings) AS total_job_openings,
    ROUND(AVG(salary),0) AS avg_salary,
    ROUND(AVG(ai_risk_score),2) AS avg_ai_risk
FROM future_jobs
GROUP BY job_title
HAVING AVG(ai_risk_score) <= 0.40
ORDER BY avg_salary DESC
LIMIT 10;