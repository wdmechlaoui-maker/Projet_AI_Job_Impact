SELECT 
    country, -- Assure-toi que c'est le nom du pays (ex: 'Germany', 'France') ou le code ISO
    ROUND(AVG(digital_score), 2) AS avg_digitalization
FROM 
    eurostat_isoc
GROUP BY 
    country;