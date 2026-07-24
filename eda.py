import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load Dataset
df = pd.read_csv("dataset/lifestyle.csv")

print("=" * 60)
print("LIFESYNC AI - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nFirst 5 Rows\n")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nSummary Statistics")
print(df.describe())


# ====================================================
# PRODUCTIVITY DISTRIBUTION
# ====================================================

plt.figure(figsize=(8,5))

plt.hist(df["productivity_score"], bins=30)

plt.title("Productivity Score Distribution")
plt.xlabel("Productivity Score")
plt.ylabel("Frequency")

plt.grid(True)

plt.savefig("images/productivity_distribution.png")

plt.close()

print("✔ Productivity Distribution Saved")


# ====================================================
# SLEEP HOURS DISTRIBUTION
# ====================================================

plt.figure(figsize=(8,5))

plt.hist(df["sleep_hours"], bins=20)

plt.title("Sleep Hours Distribution")
plt.xlabel("Sleep Hours")
plt.ylabel("Students")

plt.grid(True)

plt.savefig("images/sleep_distribution.png")

plt.close()

print("✔ Sleep Distribution Saved")

# ====================================================
# STUDY HOURS VS PRODUCTIVITY
# ====================================================

plt.figure(figsize=(8,5))

plt.scatter(
    df["study_hours_per_day"],
    df["productivity_score"],
    alpha=0.5
)

plt.title("Study Hours vs Productivity")

plt.xlabel("Study Hours")

plt.ylabel("Productivity")

plt.grid(True)

plt.savefig("images/study_vs_productivity.png")

plt.close()

print("✔ Scatter Plot Saved")

# ====================================================
# GENDER ANALYSIS
# ====================================================

gender_avg = df.groupby("gender")["productivity_score"].mean()

plt.figure(figsize=(6,5))

gender_avg.plot(kind="bar")

plt.title("Average Productivity by Gender")

plt.ylabel("Average Productivity")

plt.grid(True)

plt.savefig("images/gender_productivity.png")

plt.close()

print("✔ Gender Chart Saved")

# ====================================================
# BOXPLOT
# ====================================================

plt.figure(figsize=(6,5))

plt.boxplot(df["sleep_hours"])

plt.title("Sleep Hours Boxplot")

plt.ylabel("Sleep Hours")

plt.savefig("images/sleep_boxplot.png")

plt.close()

print("✔ Boxplot Saved")

# ====================================================
# CORRELATION HEATMAP
# ====================================================

corr = df.corr(numeric_only=True)

plt.figure(figsize=(12,10))

plt.imshow(corr, cmap="coolwarm", aspect="auto")

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)

plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png")

plt.close()

print("✔ Heatmap Saved")

plt.figure(figsize=(8,5))

plt.hist(df["exercise_minutes"], bins=25)

plt.title("Exercise Minutes Distribution")

plt.xlabel("Exercise Minutes")

plt.ylabel("Students")

plt.grid(True)

plt.savefig("images/exercise_distribution.png")

plt.close()

print("✔ Exercise Distribution Saved")

plt.figure(figsize=(8,5))

plt.hist(df["stress_level"], bins=10)

plt.title("Stress Level Distribution")

plt.xlabel("Stress Level")

plt.ylabel("Students")

plt.grid(True)

plt.savefig("images/stress_distribution.png")

plt.close()

print("✔ Stress Distribution Saved")
plt.figure(figsize=(8,5))

plt.hist(df["stress_level"], bins=10)

plt.title("Stress Level Distribution")

plt.xlabel("Stress Level")

plt.ylabel("Students")

plt.grid(True)

plt.savefig("images/stress_distribution.png")

plt.close()

print("✔ Stress Distribution Saved")

plt.figure(figsize=(8,5))

plt.hist(df["attendance_percentage"], bins=20)

plt.title("Attendance Distribution")

plt.xlabel("Attendance %")

plt.ylabel("Students")

plt.grid(True)

plt.savefig("images/attendance_distribution.png")

plt.close()

print("✔ Attendance Distribution Saved")