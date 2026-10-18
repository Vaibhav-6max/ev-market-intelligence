
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/clean/ev_population_clean.csv") # Load cleaned dataset


trend = (
    df.groupby(["Model Year", "Electric Vehicle Type"])
    .size()
    .unstack(fill_value=0)
    .sort_index()
) # Count EV records by model year and vehicle type

print("EV records by model year and vehicle type:")
print(trend.to_string())

# Save the summary
trend.to_csv("outputs/ev_records_by_year_type.csv")

# Plot the trend
ax = trend.plot(
    kind="line",
    marker="o",
    figsize=(12, 6)
)

ax.set_title("Washington EV Records by Model Year and Vehicle Type")
ax.set_xlabel("Model Year")
ax.set_ylabel("Number of Records")
ax.grid(True, alpha=0.3)
ax.legend(title="Vehicle Type")

plt.tight_layout()
plt.savefig("outputs/ev_records_by_year_type.png", dpi=300)
plt.show()

print("\nSaved summary: outputs/ev_records_by_year_type.csv")
print("Saved chart: outputs/ev_records_by_year_type.png")

