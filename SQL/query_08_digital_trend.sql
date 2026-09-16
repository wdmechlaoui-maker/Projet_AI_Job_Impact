SELECT
    year,
    ROUND(AVG(digital_score),2) AS avg_digital_score
FROM eurostat_isoc
WHERE skill_domain = 'Overall Digital Skills'
AND skill_level = 'At Least Basic'
GROUP BY year
ORDER BY year;