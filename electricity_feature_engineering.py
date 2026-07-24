import pandas as pd

# Load Dataset
df = pd.read_csv("dataset/electricity.csv")

print("Dataset Loaded Successfully")

# ---------------------------------------
# Feature 1: Total Appliances
# ---------------------------------------

df["total_appliances"] = (
    df["ac_count"] +
    df["refrigerator"] +
    df["washing_machine"] +
    df["geyser"] +
    df["laptop_count"] +
    df["tv_count"]
)

# ---------------------------------------
# Feature 2: Units Per Family Member
# ---------------------------------------

df["units_per_member"] = (
    df["monthly_units"] /
    df["family_members"]
)

# ---------------------------------------
# Feature 3: Bill Per Unit
# ---------------------------------------

df["bill_per_unit"] = (
    df["electricity_bill"] /
    df["monthly_units"]
)

# ---------------------------------------
# Feature 4: Room Density
# ---------------------------------------

df["room_density"] = (
    df["family_members"] /
    df["rooms"]
)

# ---------------------------------------
# Feature 5: Consumption Category
# ---------------------------------------

def consumption_category(units):

    if units < 200:
        return "Low"

    elif units < 400:
        return "Medium"

    elif units < 600:
        return "High"

    else:
        return "Very High"

df["consumption_category"] = df["monthly_units"].apply(consumption_category)

# ---------------------------------------
# Feature 6: Energy Efficiency Score
# ---------------------------------------

df["energy_efficiency_score"] = (
    100
    - (df["bill_per_unit"] * 10)
    - (df["ac_count"] * 2)
)

df["energy_efficiency_score"] = (
    df["energy_efficiency_score"]
    .clip(0,100)
)

# ---------------------------------------
# Save New Dataset
# ---------------------------------------

df.to_csv(
    "dataset/electricity_engineered.csv",
    index=False
)

print("\nNew Shape:")
print(df.shape)

print("\nNew Columns:")
print(df.columns)

print("\nFirst Five Rows:")
print(df.head())

print("\n✅ Feature Engineering Completed Successfully!")