
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/clean/ev_population_clean.csv")

# 1. Top 10 manufacturers
top_makes = df["Make"].value_counts().head(10)

print("TOP 10 EV MANUFACTURERS")
print(top_makes.to_string())

# 2. Top 10 EV models
top_models = (
    df.groupby(["Make", "Model"])
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 EV MODELS")
print(top_models.to_string())

# 3. Vehicle type distribution by manufacturer
make_type = pd.crosstab(
    df["Make"],
    df["Electric Vehicle Type"]
)

make_type["Total_Records"] = make_type.sum(axis=1)

make_type = make_type.sort_values(
    "Total_Records",
    ascending=False
)

print("\nVEHICLE TYPE BY TOP 10 MANUFACTURERS")
print(make_type.head(10).to_string())

# Save results
top_makes.rename("EV_Records").to_csv(
    "outputs/top_ev_manufacturers.csv"
)

top_models.rename("EV_Records").to_csv(
    "outputs/top_ev_models.csv"
)

make_type.to_csv(
    "outputs/ev_type_by_manufacturer.csv"
)

print("\nSaved three reports in the outputs folder.")
