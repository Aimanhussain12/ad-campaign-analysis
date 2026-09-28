# Facebook Ad Campaign Analysis

Analysis of real, anonymized Facebook ad campaign data to find which audiences bring sales at the lowest cost.

**Data:** [Sales Conversion Optimization](https://www.kaggle.com/datasets/loveall/clicks-conversion-tracking) (Kaggle). 1,143 ads across 3 campaigns, from a 2017-era Facebook campaign, so it reflects that period, not today's ad market.

**Live dashboard:** open `dashboard.html` (or host it with GitHub Pages).

## What's inside
- `analysis.py` - loads the data, validates it (missing values, duplicates, impossible values), calculates metrics, saves a chart
- `dashboard.html` - interactive dashboard with campaign filter, KPI cards and charts
- `KAG_conversion_data.csv` - the raw dataset
- `segment_performance.png` - chart output

## Metrics
- **CTR** = clicks / impressions (is the ad catching attention?)
- **CPA (cost per sale)** = spend / approved conversions (what does one sale cost?)
- **Enquiry-to-sale rate** = approved conversions / total enquiries

## Key findings
| Segment | Cost per sale |
|---|---|
| Age 30-34 | $30.88 |
| Age 35-39 | $53.68 |
| Age 40-44 | $68.18 |
| Age 45-49 | $99.76 |
| Men | $41.44 |
| Women | $69.70 |

1. **Younger audiences convert much cheaper.** Ages 30-34 cost about a third as much per sale as ages 45-49.
2. **Older audiences click more but buy less.** CTR rises with age (0.014% to 0.022%), but sales do not follow. They click, then don't buy.
3. **Men convert better; women click more.** Men cost $41 per sale vs $70 for women, though women have the higher CTR.
4. **Best segment: men 30-34 at $25.56 per sale. Worst: women 45-49 at $119.94.**
5. **Campaign 1178 took about 95% of the $58.7k spend** at $63.83 per sale, versus $15.81 for campaign 936. Campaign 916 is too small (about $150) to judge.

## Recommendations
- Shift budget from ages 45-49 (especially women) toward ages 30-39.
- For older audiences, test a different offer or landing page. Clicks are not the problem, conversion is.
- Investigate why campaign 1178 costs 4x more per sale than 936 before spending more on it.

## Limitations
- The data has no dates, so trends over time cannot be analyzed.
- Only 4 age groups and 2 genders are included.
- Cost per sale is a blended figure. Ads with zero sales are included, which is realistic.

## Run it
```
pip install pandas matplotlib
python analysis.py
```
