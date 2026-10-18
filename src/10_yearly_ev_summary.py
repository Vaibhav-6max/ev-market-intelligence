
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/clean/ev_population_clean.csv")

summary = (
    df.groupby(["Model Year", "Electric Vehicle Type"])
    .size()
    .unstack(fill_value=0)
) # Count records by model year and vehicle type


summary = summary.rename(columns={
    "Battery Electric Vehicle (BEV)": "BEV_Records",
    "Plug-in Hybrid Electric Vehicle (PHEV)": "PHEV_Records"
}) # Rename columns for easier analysis


summary["Total_Records"] = (
    summary["BEV_Records"] + summary["PHEV_Records"]
) # Calculate totals and BEV share

summary["BEV_Share_Percent"] = (
    summary["BEV_Records"] / summary["Total_Records"] * 100
).round(2)

print("Yearly EV records summary:")
print(summary.to_string())

# Save the summary
summary.to_csv("outputs/yearly_ev_summary.csv")

print("\nSaved: outputs/yearly_ev_summary.csv")
