import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning Model Comparison")
st.markdown("---")
results = pd.read_csv("models/model_results.csv")
ranking = pd.read_csv("models/model_ranking.csv")
st.subheader("📋 Model Performance Table")

st.dataframe(results, use_container_width=True)
best = ranking.iloc[0]

st.success(f"""
🏆 Best Model

Model : {best['Model']}

R² Score : {best['R2 Score']:.4f}
""")
st.subheader("📊 R² Score Comparison")

fig = px.bar(
    results,
    x="Model",
    y="R2 Score",
    color="R2 Score",
    text="R2 Score",
    title="Model Accuracy Comparison"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("📉 RMSE Comparison")

fig = px.bar(
    results,
    x="Model",
    y="RMSE",
    color="RMSE",
    text="RMSE"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("📉 MAE Comparison")

fig = px.bar(
    results,
    x="Model",
    y="MAE",
    color="MAE",
    text="MAE"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("📉 MSE Comparison")

fig = px.bar(
    results,
    x="Model",
    y="MSE",
    color="MSE",
    text="MSE"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("⭐ Feature Importance")

st.image(
    "images/feature_importance.png",
    use_container_width=True
)
col1, col2 = st.columns(2)

with col1:

    st.image(
        "images/actual_vs_predicted.png",
        caption="Actual vs Predicted",
        use_container_width=True
    )

with col2:

    st.image(
        "images/residual_analysis.png",
        caption="Residual Analysis",
        use_container_width=True
    )

    st.subheader("🥇 Model Ranking")

st.dataframe(ranking, use_container_width=True)
st.markdown("---")

st.success("""
✅ Multiple Machine Learning models were trained and evaluated.

The best-performing model was automatically selected and saved.

The evaluation metrics include:

• R² Score

• MAE

• RMSE

• MSE
""")
