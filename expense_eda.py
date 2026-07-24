import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("dataset/data.csv")

# ==========================================
# Create Total Expense Column
# ==========================================

df["Total_Expense"] = (
    df["Rent"]
    + df["Loan_Repayment"]
    + df["Insurance"]
    + df["Groceries"]
    + df["Transport"]
    + df["Eating_Out"]
    + df["Entertainment"]
    + df["Utilities"]
    + df["Healthcare"]
    + df["Education"]
    + df["Miscellaneous"]
)

# ==========================================
# Basic Information
# ==========================================

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET INFO ==========")
print(df.info())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== STATISTICS ==========")
print(df.describe())

# ==========================================
# Chart 1 : Income Distribution
# ==========================================

plt.figure(figsize=(8,5))
plt.hist(df["Income"], bins=30)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("images/income_distribution.png")
plt.close()

print("✅ Income Distribution Saved")

# ==========================================
# Chart 2 : Total Expense Distribution
# ==========================================

plt.figure(figsize=(8,5))
plt.hist(df["Total_Expense"], bins=30)
plt.title("Total Expense Distribution")
plt.xlabel("Total Expense")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("images/total_expense_distribution.png")
plt.close()

print("✅ Total Expense Distribution Saved")

# ==========================================
# Chart 3 : Income vs Expense
# ==========================================

plt.figure(figsize=(8,5))
plt.scatter(df["Income"], df["Total_Expense"])
plt.title("Income vs Total Expense")
plt.xlabel("Income")
plt.ylabel("Total Expense")
plt.grid(True)

plt.savefig("images/income_vs_expense.png")
plt.close()

print("✅ Income vs Expense Saved")

# ==========================================
# Chart 4 : Desired Savings
# ==========================================

plt.figure(figsize=(8,5))
plt.hist(df["Desired_Savings"], bins=30)
plt.title("Desired Savings Distribution")
plt.xlabel("Desired Savings")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("images/desired_savings_distribution.png")
plt.close()

print("✅ Desired Savings Saved")

# ==========================================
# Chart 5 : Disposable Income
# ==========================================

plt.figure(figsize=(8,5))
plt.hist(df["Disposable_Income"], bins=30)
plt.title("Disposable Income Distribution")
plt.xlabel("Disposable Income")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("images/disposable_income_distribution.png")
plt.close()

print("✅ Disposable Income Saved")

# ==========================================
# Chart 6 : Age Distribution
# ==========================================

plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.grid(True)

plt.savefig("images/age_distribution.png")
plt.close()

print("✅ Age Distribution Saved")

# ==========================================
# Chart 7 : Occupation Count
# ==========================================

plt.figure(figsize=(10,5))

df["Occupation"].value_counts().plot(kind="bar")

plt.title("Occupation Distribution")
plt.xlabel("Occupation")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/occupation_distribution.png")
plt.close()

print("✅ Occupation Distribution Saved")

# ==========================================
# Chart 8 : City Tier Distribution
# ==========================================

plt.figure(figsize=(6,5))

df["City_Tier"].value_counts().plot(kind="bar")

plt.title("City Tier Distribution")

plt.tight_layout()

plt.savefig("images/city_tier_distribution.png")
plt.close()

print("✅ City Tier Distribution Saved")

# ==========================================
# Chart 9 : Correlation Heatmap
# ==========================================

corr = df.select_dtypes(include="number").corr()

plt.figure(figsize=(14,12))

plt.imshow(corr, cmap="coolwarm")

plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/expense_heatmap.png")
plt.close()

print("✅ Correlation Heatmap Saved")

# ==========================================
# Chart 10 : Expense Boxplot
# ==========================================

plt.figure(figsize=(6,5))

plt.boxplot(df["Total_Expense"])

plt.title("Total Expense Boxplot")

plt.savefig("images/expense_boxplot.png")
plt.close()

print("✅ Expense Boxplot Saved")

# ==========================================
# Finished
# ==========================================

print("\n========================================")
print("🎉 Expense EDA Completed Successfully")
print("📁 All Charts Saved Inside images Folder")
print("========================================")