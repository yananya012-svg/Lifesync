import pandas as pd

# Load Dataset
df = pd.read_csv("dataset/data.csv")

# -----------------------------
# Create Total Expense
# -----------------------------
df["Total_Expense"] = (
    df["Rent"] +
    df["Loan_Repayment"] +
    df["Insurance"] +
    df["Groceries"] +
    df["Transport"] +
    df["Eating_Out"] +
    df["Entertainment"] +
    df["Utilities"] +
    df["Healthcare"] +
    df["Education"] +
    df["Miscellaneous"]
)

# -----------------------------
# Savings Rate
# -----------------------------
df["Savings_Rate"] = (
    df["Desired_Savings"] / df["Income"]
)

# -----------------------------
# Expense Ratio
# -----------------------------
df["Expense_Ratio"] = (
    df["Total_Expense"] / df["Income"]
)

# -----------------------------
# Financial Balance
# -----------------------------
df["Financial_Balance"] = (
    df["Income"] - df["Total_Expense"]
)

# -----------------------------
# Expense Category
# -----------------------------
df["Expense_Category"] = pd.cut(
    df["Total_Expense"],
    bins=[0, 20000, 40000, 60000, 1000000],
    labels=["Low", "Medium", "High", "Very High"]
)

# -----------------------------
# Display New Data
# -----------------------------
print("\nFirst 5 Rows:\n")
print(df.head())

print("\nNew Columns Added:\n")
print(df.columns)

# -----------------------------
# Save New Dataset
# -----------------------------
df.to_csv(
    "dataset/expense_engineered.csv",
    index=False
)

print("\n✅ Feature Engineering Completed Successfully!")
print("New dataset saved as: dataset/expense_engineered.csv")
