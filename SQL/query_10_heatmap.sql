SELECT 
    country,
    ai_risk_category AS risk_level,
    SUM(job_openings) AS total_openings,
    ROUND(AVG(salary), 0) AS average_salary
FROM 
    future_jobs
WHERE 
    country IS NOT NULL AND country != ''
    AND ai_risk_category IS NOT NULL AND ai_risk_category != ''
GROUP BY 
    country,
    ai_risk_category;