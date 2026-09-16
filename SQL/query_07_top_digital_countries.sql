SELECT
    country,
    ROUND(AVG(digital_score),2) AS avg_digital_score
FROM eurostat_isoc
WHERE skill_domain = 'Overall Digital Skills'
AND skill_level = 'At Least Basic'
GROUP BY country
ORDER BY avg_digital_score DESC
LIMIT 10;