
import pandas as pd


df = pd.read_csv("data/clean/ev_population_clean.csv") # Load cleaned dataset

# Select battery electric vehicles
bev = df[
    df["Electric Vehicle Type"]
    == "Battery Electric Vehicle (BEV)"
].copy() # Make a separate copy so changes don't affect df


# Mark each vehicle's range status
bev["Range Status"] = "Positive" # Assume the range is positive initially


bev.loc[bev["Electric Range"] == 0, "Range Status"] = "Zero" # Mark vehicles with zero range
bev.loc[bev["Electric Range"].isna(), "Range Status"] = "Missing" # Mark vehicles with no range value

# Count each range status for every model year
summary = pd.crosstab(
    bev["Model Year"],
    bev["Range Status"]
)

summary["Total"] = summary.sum(axis=1)  # Add up all range categories for each year

summary["Zero Percentage"] = (
    summary["Zero"] / summary["Total"] * 100
).round(2) # Keep the percentage to two decimal places

print("BEV electric range by model year:")
print(summary.to_string())

print("\nRecent BEV records from 2023 onward:")
print(summary.loc[summary.index >= 2023].to_string())
