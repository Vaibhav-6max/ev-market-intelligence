
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/clean/ev_population_clean.csv")

# Count records by model year and vehicle type
yearly = (
    df.groupby("Model Year")
    .agg(
        Total_EV_Records=("DOL Vehicle ID", "count"),
        Unique_Makes=("Make", "nunique"),
        Unique_Models=("Model", "nunique")
    )
    .sort_index()
)

# BEV and PHEV counts by model year
vehicle_counts = pd.crosstab(
    df["Model Year"],
    df["Electric Vehicle Type"]
)

yearly["BEV_Records"] = vehicle_counts.get(
    "Battery Electric Vehicle (BEV)", 0
)

yearly["PHEV_Records"] = vehicle_counts.get(
    "Plug-in Hybrid Electric Vehicle (PHEV)", 0
)

# Percentage of BEVs among records for each model year
yearly["BEV_Share_Percent"] = (
    yearly["BEV_Records"] / yearly["Total_EV_Records"] * 100
).round(2)

print("EV Market Insights by Model Year:")
print(yearly.to_string())

# Save results
yearly.to_csv("outputs/ev_market_insights.csv")

print("\nSaved: outputs/ev_market_insights.csv")

# Identify the model year with the most records
peak_year = yearly["Total_EV_Records"].idxmax()
peak_count = yearly["Total_EV_Records"].max()

print(f"\nModel year with the most records: {peak_year}")
print(f"Number of records: {peak_count:,}")
