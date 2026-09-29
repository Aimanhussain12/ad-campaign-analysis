-- Same analysis as analysis.py, written in SQL.
-- Table: ads (load KAG_conversion_data.csv into a table named "ads")
-- Columns: xyz_campaign_id, age, gender, interest, Impressions, Clicks,
--          Spent, Total_Conversion, Approved_Conversion

-- 1. Cost per sale by campaign
SELECT xyz_campaign_id AS campaign,
       COUNT(*) AS ads,
       ROUND(SUM(Spent), 2) AS spend,
       SUM(Approved_Conversion) AS sales,
       ROUND(SUM(Spent) * 1.0 / SUM(Approved_Conversion), 2) AS cost_per_sale
FROM ads
GROUP BY xyz_campaign_id
ORDER BY cost_per_sale;

-- 2. Cost per sale and click-through rate by age group
SELECT age,
       ROUND(SUM(Clicks) * 100.0 / SUM(Impressions), 3) AS ctr_pct,
       ROUND(SUM(Spent) * 1.0 / SUM(Approved_Conversion), 2) AS cost_per_sale
FROM ads
GROUP BY age
ORDER BY cost_per_sale;

-- 3. Cost per sale by gender
SELECT gender,
       ROUND(SUM(Spent) * 1.0 / SUM(Approved_Conversion), 2) AS cost_per_sale
FROM ads
GROUP BY gender;

-- 4. Best and worst age + gender segments (top 3 cheapest)
SELECT age, gender,
       ROUND(SUM(Spent) * 1.0 / SUM(Approved_Conversion), 2) AS cost_per_sale
FROM ads
GROUP BY age, gender
ORDER BY cost_per_sale
LIMIT 3;

-- 5. Label each ad's efficiency with CASE
SELECT CASE
         WHEN Approved_Conversion = 0 THEN 'No sales'
         WHEN Spent * 1.0 / Approved_Conversion < 25 THEN 'Efficient'
         ELSE 'Expensive'
       END AS ad_group,
       COUNT(*) AS ads
FROM ads
GROUP BY ad_group;
