import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor
)

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv("dataset/expense_engineered.csv")

print("\nDataset Loaded Successfully\n")
print(df.head())

# ---------------------------------
# Encode Categorical Columns
# ---------------------------------

# ---------------------------------
# Encode Categorical Columns
# ---------------------------------

encoders = {}

for col in df.select_dtypes(include=["object", "string"]).columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

print("\nCategorical Columns Encoded Successfully!")
# ---------------------------------

# Select Features
# (No Data Leakage)
# ---------------------------------

X = df[
    [
        "Income",
        "Age",
        "Dependents",
        "Occupation",
        "City_Tier",
        "Desired_Savings_Percentage"
    ]
]

# Target

y = df["Total_Expense"]

# ---------------------------------
# Train Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ---------------------------------
# Machine Learning Models
# ---------------------------------

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    ),

    "Extra Trees": ExtraTreesRegressor(
        n_estimators=100,
        random_state=42
    )
}

results = []

best_model = None

best_score = -999

# ---------------------------------
# Train Models
# ---------------------------------

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    r2 = r2_score(y_test, prediction)

    mae = mean_absolute_error(y_test, prediction)

    mse = mean_squared_error(y_test, prediction)

    rmse = mse ** 0.5

    results.append(
        [
            name,
            round(r2,4),
            round(mae,2),
            round(rmse,2)
        ]
    )

    print("\n===================================")
    print(name)
    print("===================================")

    print("R² Score :", round(r2,4))

    print("MAE      :", round(mae,2))

    print("RMSE     :", round(rmse,2))

    if r2 > best_score:

        best_score = r2

        best_model = model

# ---------------------------------
# ---------------------------------
# Save Best Model
# ---------------------------------

joblib.dump(
    best_model,
    "models/expense_model.pkl"
)

print("\nBest Model Saved Successfully!")

# ---------------------------------
# Save Label Encoders
# ---------------------------------

joblib.dump(
    encoders,
    "models/expense_encoders.pkl"
)

print("Label Encoders Saved Successfully!")

# ---------------------------------
# Save Results
# ---------------------------------

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "R2 Score",
        "MAE",
        "RMSE"
    ]
)

results_df.to_csv(
    "models/expense_model_results.csv",
    index=False
)

print("\nModel Comparison")
print(results_df)

print("\nExpense Model Training Completed Successfully!")