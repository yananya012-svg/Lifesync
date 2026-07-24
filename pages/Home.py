import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

st.title("🌱 LifeSync AI")
st.subheader("Personal Lifestyle & Productivity Optimization Platform")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Dataset Size", "20,000")

with col2:
    st.metric("🤖 ML Models", "5")

with col3:
    st.metric("📈 Features", "23")

st.markdown("---")

st.header("🎯 Project Objective")

st.write("""
LifeSync AI is a Machine Learning based platform that predicts a user's productivity
using their daily lifestyle habits.

The project analyzes:
- 📚 Study Hours
- 😴 Sleep Hours
- 📱 Screen Time
- 💪 Exercise
- 😌 Stress Level
- 🎯 Focus Score
- 📈 Productivity Score
""")

st.markdown("---")

st.header("⚙️ Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.success("Python")
    st.success("Pandas")
    st.success("NumPy")

with tech2:
    st.success("Scikit-Learn")
    st.success("Matplotlib")
    st.success("Plotly")

with tech3:
    st.success("Streamlit")
    st.success("Joblib")
    st.success("Machine Learning")

st.markdown("---")

st.header("🔄 Project Workflow")

st.info("""
Dataset ➜ EDA ➜ Feature Engineering ➜ Model Training ➜ Model Evaluation ➜ Prediction ➜ AI Insights
""")

st.markdown("---")

st.success("✅ Project Ready for Prediction")