import pandas as pd
import numpy as np

np.random.seed(42)

rows = 20000

house_id = np.arange(1, rows + 1)

monthly_units = np.random.randint(80, 900, rows)

house_type = np.random.choice(
    ["Apartment", "Villa", "Independent House"],
    rows
)

city = np.random.choice(
    ["Tier_1", "Tier_2", "Tier_3"],
    rows
)

family_members = np.random.randint(1, 8, rows)

rooms = np.random.randint(1, 7, rows)

ac_count = np.random.randint(0, 4, rows)

refrigerator = np.random.randint(0, 2, rows)

washing_machine = np.random.randint(0, 2, rows)

geyser = np.random.randint(0, 2, rows)

laptop_count = np.random.randint(0, 5, rows)

tv_count = np.random.randint(1, 4, rows)

work_from_home = np.random.choice(
    ["Yes", "No"],
    rows
)

solar_panel = np.random.choice(
    ["Yes", "No"],
    rows
)

bill = (
    monthly_units * 7
    + ac_count * 900
    + refrigerator * 300
    + washing_machine * 450
    + geyser * 600
    + laptop_count * 150
    + tv_count * 180
    - np.where(solar_panel == "Yes", 1200, 0)
    + np.random.normal(0, 400, rows)
)

bill = np.round(bill, 2)

df = pd.DataFrame({

    "house_id": house_id,
    "monthly_units": monthly_units,
    "house_type": house_type,
    "city": city,
    "family_members": family_members,
    "rooms": rooms,
    "ac_count": ac_count,
    "refrigerator": refrigerator,
    "washing_machine": washing_machine,
    "geyser": geyser,
    "laptop_count": laptop_count,
    "tv_count": tv_count,
    "work_from_home": work_from_home,
    "solar_panel": solar_panel,
    "electricity_bill": bill

})

df.to_csv(
    "dataset/electricity.csv",
    index=False
)

print(df.head())

print("\nDataset Shape:", df.shape)

print("\nDataset Saved Successfully!")