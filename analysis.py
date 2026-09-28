"""Facebook ad campaign analysis (real Kaggle data).
Run: python analysis.py
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. LOAD -----------------------------------------------------------
df = pd.read_csv("KAG_conversion_data.csv")

# 2. CLEAN & VALIDATE ----------------------------------------------
# Real data can be messy, so check before trusting it.
print("Rows:", len(df))
print("Missing values:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
assert (df["Approved_Conversion"] <= df["Total_Conversion"]).all(), "approved > total?"
assert (df["Clicks"] <= df["Impressions"]).all(), "clicks > impressions?"

df = df.rename(columns={
    "xyz_campaign_id": "campaign",
    "Total_Conversion": "enquiries",
    "Approved_Conversion": "sales",
    "Spent": "spend",
})
df["campaign"] = df["campaign"].astype(str)

# 3. METRICS --------------------------------------------------------
def add_metrics(g):
    g = g.copy()
    g["CTR_%"] = g["Clicks"] / g["Impressions"] * 100   # attention
    g["CPC"] = g["spend"] / g["Clicks"]                 # cost per click
    g["CPA"] = g["spend"] / g["sales"]                  # cost per sale
    g["enq_to_sale_%"] = g["sales"] / g["enquiries"] * 100
    return g.round(3)

cols = ["Impressions", "Clicks", "spend", "enquiries", "sales"]
by = lambda k: add_metrics(df.groupby(k)[cols].sum())

for key in ["campaign", "age", "gender"]:
    print(f"\n=== By {key} ===")
    print(by(key).to_string())

seg = by(["age", "gender"]).sort_values("CPA")
print("\n=== Best 3 / worst 3 age+gender segments by CPA ===")
print(seg.head(3).to_string()); print(seg.tail(3).to_string())

# 4. CHART ----------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
a = by("age")["CPA"]; ax[0].bar(a.index, a.values, color="#1877f2")
ax[0].set_title("Cost per sale by age group ($)")
g = by("gender")["CPA"]; ax[1].bar(g.index, g.values, color=["#e91e63", "#1877f2"])
ax[1].set_title("Cost per sale by gender ($)")
plt.tight_layout(); plt.savefig("segment_performance.png", dpi=120)
print("\nSaved segment_performance.png")
