import os
import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

os.makedirs("images", exist_ok=True)

df = pd.read_csv(
    "dataset/lifestyle_engineered.csv"
)

print(df.head())

encoder = LabelEncoder()

categorical_columns = [
    "gender",
    "sleep_quality",
    "exercise_level",
    "stress_category"
]

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

    X = df.drop(
    [
        "student_id",
        "productivity_score"
    ],
    axis=1
)

y = df["productivity_score"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


model.fit(
    X_train,
    y_train
)


prediction = model.predict(X_test)

plt.figure(figsize=(8,5))

plt.scatter(
    y_test,
    prediction,
    alpha=0.5
)


plt.xlabel("Actual Productivity")

plt.ylabel("Predicted Productivity")

plt.title(
    "Actual vs Predicted Productivity"
)


plt.grid(True)


plt.savefig(
    "images/actual_vs_predicted.png"
)


plt.close()


print("✔ Actual vs Predicted Saved")

residuals = y_test - prediction


plt.figure(figsize=(8,5))


plt.scatter(
    prediction,
    residuals,
    alpha=0.5
)


plt.axhline(
    0
)


plt.xlabel(
    "Predicted Values"
)


plt.ylabel(
    "Residual Error"
)


plt.title(
    "Residual Error Analysis"
)


plt.grid(True)


plt.savefig(
    "images/residual_analysis.png"
)


plt.close()


print("✔ Residual Analysis Saved")


plt.figure(figsize=(8,5))


plt.hist(
    residuals,
    bins=30
)


plt.title(
    "Prediction Error Distribution"
)


plt.xlabel(
    "Error"
)


plt.ylabel(
    "Frequency"
)


plt.grid(True)


plt.savefig(
    "images/error_distribution.png"
)


plt.close()


print("✔ Error Distribution Saved")


importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})


importance = importance.sort_values(
    by="Importance",
    ascending=False
)


print(importance)

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})


importance = importance.sort_values(
    by="Importance",
    ascending=False
)


print(importance)

plt.figure(figsize=(10,6))


plt.barh(
    importance["Feature"],
    importance["Importance"]
)


plt.title(
    "Feature Importance Analysis"
)


plt.xlabel(
    "Importance Score"
)


plt.tight_layout()


plt.savefig(
    "images/feature_importance.png"
)


plt.close()


print("✔ Feature Importance Saved")

results = pd.read_csv(
    "models/model_results.csv"
)


fig = px.bar(
    results,
    x="Model",
    y="R2 Score",
    title="Machine Learning Model Performance"
)


fig.write_html(
    "images/model_performance.html"
)


print("✔ Interactive Plotly Chart Saved")

