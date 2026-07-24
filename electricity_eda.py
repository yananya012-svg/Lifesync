import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("dataset/electricity.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------------
# Chart 1: Electricity Bill Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["electricity_bill"], bins=30)
plt.title("Electricity Bill Distribution")
plt.xlabel("Electricity Bill")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("images/electricity_bill_distribution.png")
plt.close()
print("✔ Electricity Bill Distribution Saved")

# ---------------------------------------
# Chart 2: Monthly Units Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["monthly_units"], bins=30)
plt.title("Monthly Units Distribution")
plt.xlabel("Monthly Units")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("images/monthly_units_distribution.png")
plt.close()
print("✔ Monthly Units Distribution Saved")

# ---------------------------------------
# Chart 3: Units vs Bill
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.scatter(df["monthly_units"], df["electricity_bill"])
plt.title("Monthly Units vs Electricity Bill")
plt.xlabel("Monthly Units")
plt.ylabel("Electricity Bill")
plt.savefig("images/units_vs_bill.png")
plt.close()
print("✔ Units vs Bill Saved")

# ---------------------------------------
# Chart 4: House Type Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
df["house_type"].value_counts().plot(kind="bar")
plt.title("House Type Distribution")
plt.ylabel("Count")
plt.savefig("images/house_type_distribution.png")
plt.close()
print("✔ House Type Distribution Saved")

# ---------------------------------------
# Chart 5: City Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
df["city"].value_counts().plot(kind="bar")
plt.title("City Distribution")
plt.ylabel("Count")
plt.savefig("images/city_distribution.png")
plt.close()
print("✔ City Distribution Saved")

# ---------------------------------------
# Chart 6: Family Members Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["family_members"], bins=10)
plt.title("Family Members Distribution")
plt.savefig("images/family_distribution.png")
plt.close()
print("✔ Family Distribution Saved")

# ---------------------------------------
# Chart 7: Rooms Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["rooms"], bins=10)
plt.title("Rooms Distribution")
plt.savefig("images/rooms_distribution.png")
plt.close()
print("✔ Rooms Distribution Saved")

# ---------------------------------------
# Chart 8: AC Count Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["ac_count"], bins=6)
plt.title("AC Count Distribution")
plt.savefig("images/ac_distribution.png")
plt.close()
print("✔ AC Distribution Saved")

# ---------------------------------------
# Chart 9: Refrigerator Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
df["refrigerator"].value_counts().plot(kind="bar")
plt.title("Refrigerator Count")
plt.savefig("images/refrigerator_distribution.png")
plt.close()
print("✔ Refrigerator Distribution Saved")

# ---------------------------------------
# Chart 10: Washing Machine Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
df["washing_machine"].value_counts().plot(kind="bar")
plt.title("Washing Machine Distribution")
plt.savefig("images/washing_machine_distribution.png")
plt.close()
print("✔ Washing Machine Distribution Saved")

# ---------------------------------------
# Chart 11: Geyser Distribution
# ---------------------------------------

plt.figure(figsize=(8,5))
df["geyser"].value_counts().plot(kind="bar")
plt.title("Geyser Distribution")
plt.savefig("images/geyser_distribution.png")
plt.close()
print("✔ Geyser Distribution Saved")

# ---------------------------------------
# Chart 12: Laptop Count
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["laptop_count"], bins=6)
plt.title("Laptop Count Distribution")
plt.savefig("images/laptop_distribution.png")
plt.close()
print("✔ Laptop Distribution Saved")

# ---------------------------------------
# Chart 13: TV Count
# ---------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["tv_count"], bins=6)
plt.title("TV Count Distribution")
plt.savefig("images/tv_distribution.png")
plt.close()
print("✔ TV Distribution Saved")

# ---------------------------------------
# Chart 14: Work From Home
# ---------------------------------------

plt.figure(figsize=(8,5))
df["work_from_home"].value_counts().plot(kind="bar")
plt.title("Work From Home")
plt.savefig("images/work_from_home.png")
plt.close()
print("✔ Work From Home Saved")

# ---------------------------------------
# Chart 15: Solar Panel
# ---------------------------------------

plt.figure(figsize=(8,5))
df["solar_panel"].value_counts().plot(kind="bar")
plt.title("Solar Panel")
plt.savefig("images/solar_panel.png")
plt.close()
print("✔ Solar Panel Saved")

# ---------------------------------------
# Chart 16: Correlation Heatmap
# ---------------------------------------

corr = df.select_dtypes(include=["number"]).corr()

plt.figure(figsize=(10,8))
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/electricity_heatmap.png")
plt.close()
print("✔ Correlation Heatmap Saved")

print("\n🎉 All Electricity EDA Charts Saved Successfully!")