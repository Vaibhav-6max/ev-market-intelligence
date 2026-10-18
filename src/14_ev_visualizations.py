
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/clean/ev_population_clean.csv")

# Create output directory if needed
from pathlib import Path
Path("outputs").mkdir(exist_ok=True)

# Chart 1: Top 10 manufacturers
top_makes = df["Make"].value_counts().head(10).sort_values()

plt.figure(figsize=(10, 6))
top_makes.plot(kind="barh")
plt.title("Top 10 EV Manufacturers in Washington State Dataset")
plt.xlabel("Number of Recorded Vehicles")
plt.ylabel("Manufacturer")
plt.tight_layout()
plt.savefig("outputs/top_10_manufacturers.png", dpi=300)
plt.close()

# Chart 2: Top 10 EV models
top_models = (
    df.groupby(["Make", "Model"])
    .size()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

model_labels = [
    f"{make} {model}" for make, model in top_models.index
]

plt.figure(figsize=(11, 7))
plt.barh(model_labels, top_models.values)
plt.title("Top 10 EV Models in Washington State Dataset")
plt.xlabel("Number of Recorded Vehicles")
plt.ylabel("Make and Model")
plt.tight_layout()
plt.savefig("outputs/top_10_ev_models.png", dpi=300)
plt.close()

# Chart 3: BEV vs PHEV by manufacturer
vehicle_types = pd.crosstab(
    df["Make"], df["Electric Vehicle Type"]
)

top_10_names = df["Make"].value_counts().head(10).index
vehicle_types = vehicle_types.loc[top_10_names]

vehicle_types = vehicle_types.rename(columns={
    "Battery Electric Vehicle (BEV)": "BEV",
    "Plug-in Hybrid Electric Vehicle (PHEV)": "PHEV"
})

vehicle_types = vehicle_types.sort_values(
    "BEV"
)

vehicle_types.plot(
    kind="barh",
    stacked=True,
    figsize=(11, 7)
)

plt.title("BEV vs PHEV Records by Top 10 Manufacturers")
plt.xlabel("Number of Recorded Vehicles")
plt.ylabel("Manufacturer")
plt.legend(title="Vehicle Type")
plt.tight_layout()
plt.savefig("outputs/bev_vs_phev_by_manufacturer.png", dpi=300)
plt.close()

print("Three charts saved in the outputs folder:")
print("1. outputs/top_10_manufacturers.png")
print("2. outputs/top_10_ev_models.png")
print("3. outputs/bev_vs_phev_by_manufacturer.png")
