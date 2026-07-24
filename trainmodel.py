import pandas as pd
import numpy as np
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

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("dataset/lifestyle_engineered.csv")

print("\nDataset Loaded Successfully\n")
print(df.head())

# ==========================================
# Encode Categorical Columns
# ==========================================

encoder = LabelEncoder()

categorical_columns = [
    "gender",
    "sleep_quality",
    "exercise_level",
    "stress_category"
]

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

print("\nCategorical Columns Encoded Successfully!")

# ==========================================
# Features and Target
# ==========================================

X = df.drop(
    [
        "student_id",
        "productivity_score",
        "final_grade"
    ],
    axis=1
)

y = df["productivity_score"]

print("\nFeature Shape :", X.shape)
print("Target Shape  :", y.shape)

# Save feature names for prediction
joblib.dump(
    X.columns.tolist(),
    "models/lifesync_features.pkl"
)

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================
# Models
# ==========================================

models = {

    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        random_state=42,
        n_estimators=100
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    ),

    "Extra Trees": ExtraTreesRegressor(
        random_state=42,
        n_estimators=100
    )

}

results = []

best_model = None
best_score = -999

# ==========================================
# Train Models
# ==========================================

for name, model in models.items():

    print("\n" + "=" * 60)
    print(name)

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    r2 = r2_score(y_test, prediction)

    mae = mean_absolute_error(y_test, prediction)

    mse = mean_squared_error(y_test, prediction)

    rmse = np.sqrt(mse)

    print("R² Score :", round(r2, 4))
    print("MAE      :", round(mae, 4))
    print("RMSE     :", round(rmse, 4))

    results.append([
        name,
        r2,
        mae,
        mse,
        rmse
    ])

    if r2 > best_score:

        best_score = r2

        best_model = model

# ==========================================
# Model Comparison Table
# ==========================================

results_df = pd.DataFrame(

    results,

    columns=[
        "Model",
        "R2 Score",
        "MAE",
        "MSE",
        "RMSE"
    ]

)

print("\n")
print(results_df)

# ==========================================
# Save Results
# ==========================================

results_df.to_csv(

    "models/model_results.csv",

    index=False

)

print("\nModel Comparison Saved Successfully!")

# ==========================================
# Save Best Model
# ==========================================

joblib.dump(

    best_model,

    "models/lifesync_model.pkl"

)

print("Best Model Saved Successfully!")

print("\nTraining Completed Successfully!")
# ==========================================
# Save Best Model Name
# ==========================================

with open("models/best_model.txt", "w") as f:
    f.write(f"Best Model : {type(best_model).__name__}\n")
    f.write(f"Best R2 Score : {best_score:.4f}")

print("Best Model Information Saved!")
# ==========================================
# Save Feature Importance
# ==========================================

try:

    feature_importance = pd.DataFrame({

        "Feature": X.columns,

        "Importance": best_model.feature_importances_

    })

    feature_importance = feature_importance.sort_values(

        by="Importance",

        ascending=False

    )

    feature_importance.to_csv(

        "models/feature_importance.csv",

        index=False

    )

    print("Feature Importance Saved!")

except:

    print("Current Best Model does not support Feature Importance.")
    # ==========================================
# Save Model Summary
# ==========================================

summary = pd.DataFrame({

    "Total Samples":[len(df)],

    "Training Samples":[len(X_train)],

    "Testing Samples":[len(X_test)],

    "Number of Features":[X.shape[1]],

    "Best R2":[best_score]

})

summary.to_csv(

    "models/model_summary.csv",

    index=False

)

print("Model Summary Saved!")
# ==========================================
# Save Label Encoders
# ==========================================

encoders = {}

for col in categorical_columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

joblib.dump(

    encoders,

    "models/label_encoders.pkl"

)

print("Label Encoders Saved!")
print("\n" + "="*60)

print("🏆 BEST MODEL")

print("="*60)

print(type(best_model).__name__)

print("R² Score :", round(best_score,4))

print("="*60)
print("\n" + "="*60)

print("✅ LifeSync AI Training Completed Successfully")

print("Files Generated:")

print("✔ lifesync_model.pkl")

print("✔ lifesync_features.pkl")

print("✔ model_results.csv")

print("✔ model_summary.csv")

print("✔ best_model.txt")

print("✔ feature_importance.csv")

print("✔ label_encoders.pkl")

print("="*60)

