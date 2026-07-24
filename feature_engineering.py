import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset/lifestyle.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Total Screen Time

df["total_screen_time"] = (
    df["phone_usage_hours"]
    + df["social_media_hours"]
    + df["youtube_hours"]
    + df["gaming_hours"]
)

print("Total Screen Time Created")

def sleep_quality(hours):
    if hours < 6:
        return "Poor"
    elif hours < 8:
        return "Good"
    else:
        return "Excellent"

df["sleep_quality"] = df["sleep_hours"].apply(sleep_quality)

print("Sleep Quality Created")

def exercise_level(minutes):
    if minutes < 30:
        return "Low"
    elif minutes < 60:
        return "Medium"
    else:
        return "High"

df["exercise_level"] = df["exercise_minutes"].apply(exercise_level)

print("Exercise Level Created")
def stress_category(level):
    if level <= 3:
        return "Low"
    elif level <= 7:
        return "Moderate"
    else:
        return "High"

df["stress_category"] = df["stress_level"].apply(stress_category)

print("Stress Category Created")

df["focus_efficiency"] = (
    df["focus_score"] / df["study_hours_per_day"]
)

print("Focus Efficiency Created")

df["lifestyle_balance_score"] = (
    df["sleep_hours"] * 2
    + df["exercise_minutes"] / 30
    - df["stress_level"]
    - df["total_screen_time"]
)

print("Lifestyle Balance Score Created")

df.to_csv(
    "dataset/lifestyle_engineered.csv",
    index=False
)

print("Feature Engineered Dataset Saved")
print(df.columns)
print(df.head())
