
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/ev_population.csv")

yearly_ev = (
    df.groupby("Model Year")
    .size()
    .reset_index(name="EV Count")
    .sort_values("Model Year")
) # Group all records by their Model Year 
#Sort the records by model year in ascending order

print("EV records by model year:")
print(yearly_ev.to_string(index=False))


plt.figure(figsize=(12, 6))  # Create a figure that is 12 inches wide and 6 inches tall
plt.bar(yearly_ev["Model Year"], yearly_ev["EV Count"])  # Create a bar chart of EV records by model year

plt.title("Electric Vehicle Records by Model Year")
plt.xlabel("Model Year")
plt.ylabel("Number of EV Records")
plt.xticks(yearly_ev["Model Year"], rotation=45)  # Show each model year and rotate labels by 45 degrees
plt.tight_layout()  # Adjust spacing so labels do not overlap or get cut off


plt.savefig("outputs/ev_by_model_year.png", dpi=300) # Save the chart as a high-resolution PNG image
plt.show()

print("\nChart saved to outputs/ev_by_model_year.png")


# Investigate recent model years
print("\nEV records for recent model years:")

recent_years = (
    df["Model Year"]
    .value_counts()
    .sort_index()
    .tail(10)
)

print(recent_years)


print("\nRecords for model years 2025, 2026, and 2027:") # Inspect the latest model-year records

recent_records = df[df["Model Year"].isin([2025, 2026, 2027])] # Keep only rows whose model year is 2025, 2026, or 2027

print(
    recent_records[
        ["Model Year", "Make", "Model", "Electric Vehicle Type"]
    ].head(15).to_string(index=False) 
) # Display the first 15 matching records without row index numbers



import pandas as pd
from pathlib import Path


df = pd.read_csv("data/raw/ev_population.csv") # Load the original dataset


clean_df = df.copy() # Make a copy so the original data stays unchanged

clean_df = clean_df.drop_duplicates() # Remove rows that are completely duplicated


text_columns = [
    "County",
    "City",
    "Vehicle Location",
    "Electric Utility",
] # Fill missing text fields with "Unknown"

for col in text_columns:
    clean_df[col] = clean_df[col].fillna("Unknown")  # Replace missing values in the current column with "Unknown"


output_path = Path("data/clean/ev_population_clean.csv")  # Define the path where the cleaned CSV will be saved
output_path.parent.mkdir(parents=True, exist_ok=True)  # Create the output folder if it does not already exist

clean_df.to_csv(output_path, index=False)  # Save the cleaned DataFrame as a CSV without row index numbers

print("Original shape:", df.shape)
print("Cleaned shape:", clean_df.shape)
print("Remaining missing values:")
print(clean_df.isnull().sum())
print("\nCleaned dataset saved to:", output_path)
