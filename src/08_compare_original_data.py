
import pandas as pd

# Load original and cleaned datasets
original = pd.read_csv("data/raw/ev_population.csv") # Load the original data
cleaned = pd.read_csv("data/clean/ev_population_clean.csv")  # Load the cleaned data

# Compare range values for recent BEVs
vehicle_type = "Battery Electric Vehicle (BEV)"

for name, df in [
    ("Original", original),
    ("Cleaned", cleaned)
]:
    bev = df[
        (df["Electric Vehicle Type"] == vehicle_type)
        & (df["Model Year"] >= 2021)
    ]

    print(f"\n{name} dataset: BEVs from 2021 onward")
    print("Total records:", len(bev))
    print("Zero ranges:", (bev["Electric Range"] == 0).sum())
    print("Positive ranges:", (bev["Electric Range"] > 0).sum())
    print("Missing ranges:", bev["Electric Range"].isna().sum())

# Inspect the original source's range values by year
print("\nOriginal BEV range statistics by model year:")
print(
    original[
        original["Electric Vehicle Type"] == vehicle_type
    ]
    .groupby("Model Year")["Electric Range"]
    .agg(["count", "median", "min", "max"])
    .tail(10)
)
