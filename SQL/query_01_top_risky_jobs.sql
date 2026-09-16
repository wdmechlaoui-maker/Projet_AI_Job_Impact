
SELECT
job_role,
ROUND(AVG(ai_risk_score_std),2) AS avg_ai_risk,
COUNT(*) AS nb_employees
FROM ai_job_impact
GROUP BY job_role
ORDER BY avg_ai_risk DESC, nb_employees DESC
LIMIT 10;

