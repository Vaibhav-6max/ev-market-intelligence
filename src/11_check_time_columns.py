
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/clean/ev_population_clean.csv")


print("Available columns:")
print(df.columns.tolist())

# Find columns related to dates or time
print("\nPotential time-related columns:")
for column in df.columns:
    if any(word in column.lower() for word in ["date", "year", "time", "registration"]):
        print(column)

# Check the model-year range
print("\nModel year range:")
print("Minimum:", df["Model Year"].min())
print("Maximum:", df["Model Year"].max())
