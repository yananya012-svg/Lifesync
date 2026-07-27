import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


st.title("📈 Machine Learning Model Comparison Dashboard")

st.write(
    "Compare the performance of all Machine Learning models used in LifeSync AI."
)

st.markdown("---")
# ----------------------------------------
# Load Model Result Files
# ----------------------------------------

try:
    lifestyle = pd.read_csv("models/model_results.csv")
except:
    lifestyle = pd.DataFrame()

try:
    expense = pd.read_csv("models/expense_model_results.csv")
except:
    expense = pd.DataFrame()

try:
    electricity = pd.read_csv("models/electricity_model_results.csv")
except:
    electricity = pd.DataFrame()
    # ----------------------------------------
# Lifestyle Models
# ----------------------------------------

st.header("🌱 Lifestyle Models")

if not lifestyle.empty:

    st.dataframe(
        lifestyle,
        use_container_width=True
    )

else:

    st.warning("Lifestyle model results not found.")

st.markdown("---")

# ----------------------------------------
# Expense Models
# ----------------------------------------

st.header("💰 Expense Models")

if not expense.empty:

    st.dataframe(
        expense,
        use_container_width=True
    )

else:

    st.warning("Expense model results not found.")

st.markdown("---")

# ----------------------------------------
# Electricity Models
# ----------------------------------------

st.header("⚡ Electricity Models")

if not electricity.empty:

    st.dataframe(
        electricity,
        use_container_width=True
    )

else:

    st.warning("Electricity model results not found.")
    # ----------------------------------------
# Combine All Models
# ----------------------------------------

frames = []

if not lifestyle.empty:

    lifestyle["Module"] = "Lifestyle"

    frames.append(lifestyle)

if not expense.empty:

    expense["Module"] = "Expense"

    frames.append(expense)

if not electricity.empty:

    electricity["Module"] = "Electricity"

    frames.append(electricity)

if len(frames) > 0:

    combined = pd.concat(
        frames,
        ignore_index=True
    )

else:

    combined = pd.DataFrame()
    # ----------------------------------------
# Combine All Models
# ----------------------------------------

frames = []

if not lifestyle.empty:

    lifestyle["Module"] = "Lifestyle"

    frames.append(lifestyle)

if not expense.empty:

    expense["Module"] = "Expense"

    frames.append(expense)

if not electricity.empty:

    electricity["Module"] = "Electricity"

    frames.append(electricity)

if len(frames) > 0:

    combined = pd.concat(
        frames,
        ignore_index=True
    )

else:

    combined = pd.DataFrame()
    # ----------------------------------------
# Overall Comparison
# ----------------------------------------

st.markdown("---")

st.header("🏆 Overall Model Comparison")

if not combined.empty:

    st.dataframe(
        combined,
        use_container_width=True
    )

else:

    st.warning("No model results available.")
    # ----------------------------------------
# Best Model
# ----------------------------------------

if not combined.empty:

    best = combined.loc[
        combined["R2 Score"].idxmax()
    ]

    st.success(f"""
🏆 Best Performing Model

📂 Module : {best['Module']}

🤖 Algorithm : {best['Model']}

📈 R² Score : {best['R2 Score']:.4f}

📉 MAE : {best['MAE']:.2f}

📊 RMSE : {best['RMSE']:.2f}
""")
    # ----------------------------------------
# R² Score Chart
# ----------------------------------------

if not combined.empty:

    st.markdown("---")

    st.header("📈 R² Score Comparison")

    fig = px.bar(

        combined,

        x="Model",

        y="R2 Score",

        color="Module",

        text="R2 Score",

        barmode="group",

        title="R² Score of All Models"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ----------------------------------------
# MAE Comparison
# ----------------------------------------

if not combined.empty:

    st.markdown("---")

    st.header("📉 MAE Comparison")

    fig = px.bar(

        combined,

        x="Model",

        y="MAE",

        color="Module",

        text="MAE",

        barmode="group",

        title="Mean Absolute Error"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ----------------------------------------
# RMSE Comparison
# ----------------------------------------

if not combined.empty:

    st.markdown("---")

    st.header("📊 RMSE Comparison")

    fig = px.bar(

        combined,

        x="Model",

        y="RMSE",

        color="Module",

        text="RMSE",

        barmode="group",

        title="Root Mean Squared Error"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ----------------------------------------
# Dashboard Metrics
# ----------------------------------------

if not combined.empty:

    st.markdown("---")

    st.header("📊 Dashboard Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Models",
            len(combined)
        )

    with c2:

        st.metric(
            "Modules",
            combined["Module"].nunique()
        )

    with c3:

        st.metric(
            "Best R²",
            round(
                combined["R2 Score"].max(),
                4
            )
        )

    with c4:

        st.metric(
            "Average R²",
            round(
                combined["R2 Score"].mean(),
                4
            )
        )
        st.markdown("---")

st.success("✅ Model Comparison Dashboard Ready")

st.caption("""

LifeSync AI

Machine Learning • Data Science • Streamlit

Developed by Ananya Yadav

""")

