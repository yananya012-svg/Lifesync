import streamlit as st

st.set_page_config(
    page_title="LifeSync AI",
    page_icon="🌱",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("🌱 LifeSync AI Platform")

st.subheader(
    "Personal Lifestyle • Expense • Electricity Intelligence"
)

st.markdown("---")

st.success(
    "🚀 Welcome to the AI Powered Personal Resource Optimization Platform"
)

st.write("""
LifeSync AI combines multiple Machine Learning models to analyze
daily lifestyle, monthly expenses and electricity usage.
The platform predicts future outcomes and provides personalized AI recommendations.
""")

st.markdown("---")

# ==========================================
# DASHBOARD METRICS
# ==========================================

st.header("📊 Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📂 Datasets",
        "3"
    )

with col2:
    st.metric(
        "🤖 ML Models",
        "15"
    )

with col3:
    st.metric(
        "📈 Visualizations",
        "40+"
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "⚡ Prediction Modules",
        "3"
    )

with col5:
    st.metric(
        "🏆 Best Accuracy",
        "99%"
    )

with col6:
    st.metric(
        "🧠 AI Recommendation Systems",
        "3"
    )

st.markdown("---")
st.header("🚀 Platform Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""
### 🌱 Lifestyle Prediction

✔ Productivity Prediction

✔ Lifestyle Analysis

✔ Stress Detection

✔ AI Suggestions
""")

with c2:

    st.success("""
### 💰 Expense Prediction

✔ Monthly Expense Prediction

✔ Savings Analysis

✔ Budget Health

✔ Financial Tips
""")

with c3:

    st.warning("""
### ⚡ Electricity Prediction

✔ Electricity Bill Prediction

✔ Energy Score

✔ Consumption Analysis

✔ Energy Saving Tips
""")

st.markdown("---")
st.header("📌 Project Workflow")

st.code("""

Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Models
      │
      ▼
Model Evaluation
      │
      ▼
Prediction
      │
      ▼
AI Recommendation System

""")

st.markdown("---")

st.header("⚙ Technologies Used")

col1,col2,col3,col4=st.columns(4)

with col1:

    st.success("Python")

    st.success("Pandas")

    st.success("NumPy")

with col2:

    st.success("Scikit-Learn")

    st.success("Joblib")

    st.success("Machine Learning")

with col3:

    st.success("Matplotlib")

    st.success("Plotly")

    st.success("Streamlit")

with col4:

    st.success("GitHub")

    st.success("VS Code")

    st.success("CSV Dataset")
    st.markdown("---")

st.header("🧭 Navigation Guide")

st.info("""

🏠 Home

📊 Lifestyle Prediction

💰 Expense Prediction

⚡ Electricity Prediction

📈 Model Comparison

🧠 AI Insights

👩‍💻 About

""")
st.markdown("---")

st.header("📈 Platform Statistics")

left,right=st.columns(2)

with left:

    st.metric(
        "Total Dataset Records",
        "60,000"
    )

    st.metric(
        "Total Features",
        "60+"
    )

    st.metric(
        "Models Trained",
        "15"
    )

with right:

    st.metric(
        "EDA Charts",
        "40+"
    )

    st.metric(
        "Prediction Pages",
        "3"
    )

    st.metric(
        "Reports Download",
        "CSV Enabled"
    )
    st.markdown("---")

st.success("✅ LifeSync AI Platform Ready")

st.caption(
    "Developed by Ananya Yadav | B.Tech AI | Machine Learning & Data Science"
)
