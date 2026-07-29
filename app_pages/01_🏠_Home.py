import streamlit as st

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Home | LifeSync AI",
    page_icon="🏠",
    layout="wide"
)

# ======================================================
# LOAD CSS
# ======================================================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ======================================================
# LOGIN CHECK
# ======================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

# ======================================================
# USER DETAILS
# ======================================================

user_name = "User"

try:
    if st.session_state.user:
        user_name = st.session_state.user[1]
except:
    pass

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.title("🌱 LifeSync AI")

    st.caption("Personal AI Analytics Platform")

    st.divider()

    st.success(f"👋 Welcome,\n\n**{user_name}**")

    st.write("🟢 Status : Online")

    st.divider()

    st.subheader("📊 Platform")

    st.metric("Datasets", "3")
    st.metric("ML Models", "15")
    st.metric("Accuracy", "99%")
    st.metric("Charts", "40+")

    st.divider()

    st.subheader("⚙ Technology")

    st.success("Python")
    st.success("Machine Learning")
    st.success("Pandas")
    st.success("NumPy")
    st.success("Scikit-Learn")
    st.success("Plotly")
    st.success("Streamlit")

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.switch_page("app.py")

    st.divider()

    st.caption("© 2026 LifeSync AI")

# ======================================================
# HEADER
# ======================================================

st.title("🌱 LifeSync AI Dashboard")

st.caption("Personal AI Analytics Platform")

st.success(f"Welcome back, {user_name}! 👋")
st.balloons()

st.info(
    """
🚀 Welcome to LifeSync AI

An Intelligent Machine Learning Platform for:

• Lifestyle Prediction

• Expense Prediction

• Electricity Consumption Prediction

• AI Recommendations
"""
)

st.divider()
st.header("🌟 Project Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Models", "15")

with col2:
    st.metric("Accuracy", "99%")

with col3:
    st.metric("Datasets", "3")

with col4:
    st.metric("Users", "Secure Login")

# ======================================================
# DASHBOARD METRICS
# ======================================================

st.header("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📂 Datasets", "3")

with col2:
    st.metric("🤖 ML Models", "15")

with col3:
    st.metric("📈 Accuracy", "99%")

with col4:
    st.metric("📊 Charts", "40+")

st.divider()

# ======================================================
# FEATURES
# ======================================================

st.header("🚀 Platform Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""
### 🌱 Lifestyle Prediction

✔ Productivity Prediction

✔ Stress Detection

✔ Lifestyle Score

✔ AI Recommendations
""")

with c2:

    st.success("""
### 💰 Expense Prediction

✔ Monthly Expenses

✔ Savings Prediction

✔ Budget Analysis

✔ Financial Advice
""")

with c3:

    st.warning("""
### ⚡ Electricity Prediction

✔ Bill Prediction

✔ Consumption Analysis

✔ Energy Score

✔ Saving Suggestions
""")

st.divider()

# ======================================================
# MACHINE LEARNING WORKFLOW
# ======================================================

st.header("📌 Machine Learning Workflow")

st.code("""
Dataset
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
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
Prediction
    │
    ▼
AI Recommendation
""")

st.divider()

# ======================================================
# TECHNOLOGY STACK
# ======================================================

st.header("⚙ Technology Stack")

a, b, c, d = st.columns(4)

with a:
    st.success("Python")
    st.success("Pandas")
    st.success("NumPy")

with b:
    st.success("Scikit-Learn")
    st.success("Joblib")
    st.success("Machine Learning")

with c:
    st.success("Matplotlib")
    st.success("Plotly")
    st.success("Streamlit")

with d:
    st.success("GitHub")
    st.success("VS Code")
    st.success("CSV Dataset")

st.divider()

# ======================================================
# PLATFORM STATISTICS
# ======================================================

st.header("📈 Platform Statistics")

left, right = st.columns(2)

with left:

    st.metric("Dataset Records", "60,000")

    st.metric("Features", "60+")

    st.metric("Prediction Modules", "3")

with right:

    st.metric("Models Trained", "15")

    st.metric("EDA Charts", "40+")

    st.metric("Download Reports", "CSV")

st.divider()

st.success("✅ LifeSync AI Platform Ready")

st.caption(
    "Developed by Ananya Yadav | B.Tech Artificial Intelligence"
)