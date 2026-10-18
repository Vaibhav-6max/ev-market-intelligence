
import pandas as pd
from pathlib import Path  #imports Python's Path class, which helps you work with file and folder paths.


df = pd.read_csv("data/raw/ev_population.csv")


clean_df = df.copy()  # Create a separate copy so the original data stays unchanged

clean_df = clean_df.drop_duplicates() # Remove completely duplicated rows


text_columns = [
    "County",
    "City",
    "Vehicle Location",
    "Electric Utility",
] # Fill missing values in text columns

for col in text_columns:
    clean_df[col] = clean_df[col].fillna("Unknown") # Replace missing values in the current column with "Unknown"


# Create output folder and save cleaned data
output_path = Path("data/clean/ev_population_clean.csv")  # Set the destination path for the cleaned CSV file
output_path.parent.mkdir(parents=True, exist_ok=True)  # Create the output folder if it does not exist


clean_df.to_csv(output_path, index=False)  # Save the cleaned data as a CSV without row index numbers


print("Original shape:", df.shape)
print("Cleaned shape:", clean_df.shape)

print("\nRemaining missing values:")
print(clean_df.isnull().sum())

print("\nCleaned dataset saved to:", output_path)
