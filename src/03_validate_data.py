
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/clean/ev_population_clean.csv")

print("Dataset shape:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Check electric range statistics
print("\nElectric Range statistics:")
print(df["Electric Range"].describe())

# Check electric range by vehicle type
print("\nElectric Range by vehicle type:")
print(
    df.groupby("Electric Vehicle Type")["Electric Range"]
    .agg(["count", "mean", "median", "min", "max"])
)

# Check for invalid negative ranges
negative_ranges = (df["Electric Range"] < 0).sum()
print("\nNegative electric range values:", negative_ranges)

# Check model years
print("\nModel year counts:")
print(df["Model Year"].value_counts().sort_index())
