import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("dataset/electricity_engineered.csv")

print("Dataset Loaded Successfully")
print(df.head())

# ---------------------------------------
# Encode Categorical Columns
# ---------------------------------------

label_encoders = {}

for col in df.select_dtypes(include=["object"]).columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

print("\nCategorical Columns Encoded Successfully!")

# ---------------------------------------
# Features and Target
# ---------------------------------------

X = df.drop(
    columns=[
        "house_id",
        "electricity_bill"
    ]
)

y = df["electricity_bill"]

# ---------------------------------------
# Train Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ---------------------------------------
# Models
# ---------------------------------------

# ---------------------------------------
# Models
# ---------------------------------------

models = {

    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42,
        max_depth=15
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=20,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=50,
        random_state=42
    ),

    "Extra Trees": ExtraTreesRegressor(
        n_estimators=20,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )

}

results = []

best_score = -999
best_model = None
best_name = ""
# ---------------------------------------
# Train Models
# ---------------------------------------

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    r2 = r2_score(y_test, pred)

    mae = mean_absolute_error(y_test, pred)

    rmse = mean_squared_error(
        y_test,
        pred
    ) ** 0.5

    print("\n====================")
    print(name)
    print("====================")

    print("R2 Score :", round(r2,4))
    print("MAE :", round(mae,2))
    print("RMSE :", round(rmse,2))

    results.append([
        name,
        r2,
        mae,
        rmse
    ])

    if r2 > best_score:

        best_score = r2

        best_model = model

        best_name = name
        # ---------------------------------------
# Save Best Model
# ---------------------------------------

joblib.dump(
    best_model,
    "models/electricity_model.pkl",
    compress=3
)

print("\nBest Model :", best_name)
print("Best Score :", round(best_score,4))


# ---------------------------------------
# Save Results
# ---------------------------------------

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

    "models/electricity_model_results.csv",

    index=False

)

print("\nModel Results Saved Successfully!")

print(results_df)