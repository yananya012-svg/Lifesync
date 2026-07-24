import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👩‍💻",
    layout="wide"
)

st.title("👩‍💻 About LifeSync AI")

st.markdown("---")

st.header("🌱 Project Overview")

st.write("""
**LifeSync AI** is a Machine Learning-based lifestyle and productivity prediction platform.

The application analyzes daily lifestyle habits such as:

- 📚 Study Hours
- 😴 Sleep Hours
- 📱 Screen Time
- 💪 Exercise
- 😌 Stress Level
- 🎯 Focus Score

Using Machine Learning, it predicts productivity and provides personalized lifestyle recommendations to help users improve their daily routine.
""")

st.markdown("---")

st.header("🚀 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.success("Python")

    st.success("NumPy")

    st.success("Pandas")

    st.success("Matplotlib")

    st.success("Plotly")

with col2:

    st.success("Scikit-Learn")

    st.success("Streamlit")

    st.success("Joblib")

    st.success("Machine Learning")

    st.success("GitHub")

st.markdown("---")

st.header("🤖 Machine Learning Workflow")

st.info("""

Dataset

⬇

Exploratory Data Analysis

⬇

Feature Engineering

⬇

Model Training

⬇

Model Evaluation

⬇

Prediction

⬇

AI Insights

""")

st.markdown("---")

st.header("📊 Machine Learning Models Used")

st.table({

"Algorithm":[

"Linear Regression",

"Decision Tree",

"Random Forest",

"Gradient Boosting",

"Extra Trees"

],

"Purpose":[

"Baseline Model",

"Tree-based Learning",

"Ensemble Learning",

"Boosting",

"High Accuracy Ensemble"

]

})

st.markdown("---")

st.header("⭐ Project Features")

st.write("""

✅ Exploratory Data Analysis

✅ Feature Engineering

✅ Multiple ML Models

✅ Model Comparison Dashboard

✅ Productivity Prediction

✅ AI Lifestyle Recommendations

✅ Interactive Streamlit Dashboard

✅ Plotly Visualizations

✅ Professional UI

""")

st.markdown("---")

st.header("📁 Project Folder Structure")

st.code("""

LifeSyncAI/

│

├── app.py

├── eda.py

├── feature_engineering.py

├── trainmodel.py

├── model_analysis.py

├── advanced_model_analysis.py

│

├── dataset/

├── images/

├── models/

├── pages/

│

├── README.md

├── requirements.txt

""")

st.markdown("---")

st.header("🌍 Future Enhancements")

st.write("""

• User Login System

• Cloud Database

• Mobile Application

• Real-time Health Tracking

• Smart Notifications

• Wearable Device Integration

• AI Chatbot

• Weekly Productivity Reports

• PDF Report Generation

• Cloud Deployment

""")

st.markdown("---")

st.header("👩‍💻 Developer")

st.write("""

**Name:** Ananya Yadav

**Degree:** B.Tech (AI)

**Project:** LifeSync AI

**Domain:** Machine Learning & Data Science

""")

st.markdown("---")

st.success("🎉 Thank you for exploring LifeSync AI!")