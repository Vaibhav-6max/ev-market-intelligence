
import pandas as pd


df = pd.read_csv("data/clean/ev_population_clean.csv")


df["Range Category"] = "Positive range" # Count zero, positive, and missing range values


# Count zero, positive, and missing range values
df.loc[df["Electric Range"] == 0, "Range Category"] = "Zero range" # Label records with a range of 0 as Zero range
df.loc[df["Electric Range"].isna(), "Range Category"] = "Missing range" # Label records with missing range values as Missing range

# Count range categories for each vehicle type
summary = pd.crosstab(
    df["Electric Vehicle Type"],
    df["Range Category"]
) # Create a frequency table comparing vehicle types and range categories

print("Range category counts by vehicle type:")
print(summary)


percentages = pd.crosstab(
    df["Electric Vehicle Type"],
    df["Range Category"],
    normalize="index"
) * 100 # Calculate percentages within each vehicle type

print("\nPercentages by vehicle type:")
print(percentages.round(2))

# Show examples of zero-range records
print("\nSample zero-range records:")
print(
    df.loc[
        df["Electric Range"] == 0,
        ["Make", "Model", "Model Year", "Electric Vehicle Type"]
    ].head(10).to_string(index=False)
)
