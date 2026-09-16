
SELECT
    industry,
    ROUND(AVG(ai_risk_score_std),2) AS avg_ai_risk,
    COUNT(*) AS nb_employees
FROM ai_job_impact
GROUP BY industry_std
ORDER BY avg_ai_risk DESC, nb_employees DESC;