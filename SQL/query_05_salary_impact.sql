SELECT
    job_role AS job_role,
    ROUND(AVG(salary_before_ai), 0) AS avg_salary_before,
    ROUND(AVG(salary_after_ai), 0) AS avg_salary_after,
    ROUND(AVG(salary_after_ai) - AVG(salary_before_ai), 0) AS salary_gain,
    ROUND(
        ((AVG(salary_after_ai) - AVG(salary_before_ai)) / AVG(salary_before_ai)) * 100, 
        2
    ) AS salary_gain_percent
FROM ai_job_impact
GROUP BY job_role
ORDER BY salary_gain_percent DESC -- On trie par le plus fort impact relatif
LIMIT 10;