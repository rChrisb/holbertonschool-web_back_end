-- old school band

SELECT band_name, 
       CASE
            WHEN formed IS NOT NULL AND split IS NOT NULL THEN EXTRACT(YEAR FROM split) - EXTRACT(YEAR FROM formed)
            WHEN formed IS NOT NULL THEN EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM formed)
            ELSE NULL
       END AS lifespan
FROM metal_bands
WHERE band_style = 'Glam rock'
ORDER BY lifespan DESC;
