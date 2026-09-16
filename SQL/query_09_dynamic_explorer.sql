SELECT 
    job_title_std AS job_title,
    experience_level,
    -- On calcule un risque moyen global pour le métier
    CASE 
        WHEN AVG(ai_risk_score) >= 0.7 THEN 'High Risk'
        WHEN AVG(ai_risk_score) >= 0.4 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_level,
    ROUND(AVG(salary), 0) AS salary,
    ROUND(AVG(ai_risk_score), 2) AS ai_risk_score,
    SUM(job_openings) AS job_openings
FROM 
    future_jobs
GROUP BY 
    job_title_std,
    experience_level; -- <-- On ne groupe plus par catégorie de risque !