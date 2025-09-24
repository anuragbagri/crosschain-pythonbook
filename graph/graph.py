import pandas as pd
import matplotlib.pyplot as plt

# Create dataset manually
data = {
    "month": [
        "2025-01-01 00:00:00.000 UTC",
        "2025-02-01 00:00:00.000 UTC",
        "2025-03-01 00:00:00.000 UTC",
        "2025-04-01 00:00:00.000 UTC",
        "2025-05-01 00:00:00.000 UTC",
        "2025-06-01 00:00:00.000 UTC"
    ],
    "new_users": [7781, 2008, 4213, 1756, 2147, 1059]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["month"] = pd.to_datetime(df["month"])  # convert to datetime

# Plot
plt.figure(figsize=(10,6))
plt.plot(df["month"], df["new_users"], marker="o", linestyle="-", color="orange")

# Labels and title
plt.title("New Users Over Time", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("New Users", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save plot for download
plt.savefig("new_users_plot.png")

# Show the plot
plt.show()

