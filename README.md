# Facebook Ad Campaign Analysis

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?logo=postgresql&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?logo=chartdotjs&logoColor=white)

**Which audiences bring sales at the lowest cost?** Analysis of real, anonymized Facebook ad data (1,143 ads, 3 campaigns), in Python and SQL, with an interactive dashboard.

**[Live Dashboard](https://aimanhussain12.github.io/ad-campaign-analysis/dashboard.html)** · **[Dataset (Kaggle)](https://www.kaggle.com/datasets/loveall/clicks-conversion-tracking)** · **[Python code](analysis.py)** · **[SQL queries](queries.sql)**

![Dashboard screenshot](dashboard.png)

## Key findings
| Segment | Cost per sale |
|---|---|
| Age 30-34 | $30.88 |
| Age 35-39 | $53.68 |
| Age 40-44 | $68.17 |
| Age 45-49 | $99.76 |
| Men | $41.44 |
| Women | $69.70 |

1. **Younger audiences convert much cheaper.** Ages 30-34 cost about a third as much per sale as ages 45-49.
2. **Older audiences click more but buy less.** Click-through rate rises with age (0.014% to 0.022%), but sales do not follow.
3. **Men convert better; women click more.** Men cost $41 per sale vs $70 for women.
4. **Best segment: men 30-34 at $25.55 per sale. Worst: women 45-49 at $119.94.**
5. **Campaign 1178 took about 95% of the $58.7k spend** at $63.83 per sale, versus $15.81 for campaign 936. Campaign 916 is too small (about $150) to judge.

## Recommendations
- Shift budget from ages 45-49 (especially women) toward ages 30-39.
- For older audiences, test a different offer or landing page. Clicks are not the problem, conversion is.
- Investigate why campaign 1178 costs 4x more per sale than 936 before spending more on it.

## Metrics used
- **CTR** = clicks / impressions (is the ad catching attention?)
- **Cost per sale** = spend / approved conversions (what does one sale cost?)
- **Enquiry-to-sale rate** = approved conversions / total enquiries

## What's inside
| File | Purpose |
|---|---|
| `analysis.py` | Loads and validates the data, calculates metrics, saves a chart |
| `queries.sql` | The same analysis in SQL (GROUP BY, CASE, ORDER BY) |
| `dashboard.html` | Interactive dashboard with campaign filter |
| `KAG_conversion_data.csv` | Raw dataset |

## Limitations
- The data is from a 2017-era campaign, so it reflects that period, not today's ad market.
- No dates in the data, so trends over time cannot be analyzed.
- Only 4 age groups and 2 genders are included.

## Run it
```
pip install pandas matplotlib
python analysis.py
```
