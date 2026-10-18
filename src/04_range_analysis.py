
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/ev_population_clean.csv")

# Show range statistics by vehicle type
print("Electric range statistics by vehicle type:")
print(
    df.groupby("Electric Vehicle Type")["Electric Range"]
    .describe()  # Calculate count, mean, standard deviation, minimum, quartiles, and maximum
    .round(2)  # Round numeric results to 2 decimal places
)

# Create separate boxplots for the two vehicle types
plt.figure(figsize=(10, 6))

df.boxplot(
    column="Electric Range",
    by="Electric Vehicle Type",
    grid=False
)

plt.title("Electric Range by Vehicle Type")
plt.suptitle("")
plt.xlabel("Vehicle Type")
plt.ylabel("Electric Range (miles)")
plt.xticks(rotation=10)
plt.tight_layout()

plt.savefig("outputs/electric_range_by_type.png", dpi=300)
plt.show()
