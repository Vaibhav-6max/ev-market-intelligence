
import pandas as pd

df = pd.read_csv("data/clean/ev_population_clean.csv")

# Check range quality for each model year and vehicle type
summary = (
    df.groupby(["Model Year", "Electric Vehicle Type"])
    .agg(
        Total_Records=("Electric Range", "size"),
        Positive_Range=("Electric Range", lambda x: (x > 0).sum()),
        Zero_Range=("Electric Range", lambda x: (x == 0).sum()),
        Missing_Range=("Electric Range", lambda x: x.isna().sum()),
        Median_Range=("Electric Range", "median"),
    )
    .reset_index()
)

print(summary.to_string(index=False))

# Save the summary for later analysis
summary.to_csv(
    "outputs/range_quality_by_year_type.csv",
    index=False
)

print("\nSaved: outputs/range_quality_by_year_type.csv") # Confirm where the summary was saved
