import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👩‍💻",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


st.title("👩‍💻 About LifeSync AI")

st.markdown("---")

st.write("""
LifeSync AI is an Artificial Intelligence platform developed to analyze
Lifestyle, Financial, and Electricity consumption patterns using
Machine Learning models.

The application predicts user behaviour and provides personalized
AI recommendations for improving daily life.
""")

# ----------------------------------------
# Developer Profile
# ----------------------------------------

st.header("👩‍💻 Developer Profile")

col1, col2 = st.columns([1, 2])

with col1:

    st.info("""
### 👩‍💻 Developer

**Ananya Yadav**

🎓 B.Tech (Artificial Intelligence)

🏫 Babu Banarasi Das University

📍 Lucknow, India
""")

with col2:

    st.markdown("""
### 💡 About Me

I am a B.Tech Artificial Intelligence student passionate about
Machine Learning, Data Science, and AI application development.

This project demonstrates practical skills in:

- 🤖 Machine Learning
- 📊 Data Analysis & Visualization
- 🌐 Streamlit Dashboard Development
- 🐍 Python Programming
- 📈 Predictive Analytics
""")

st.markdown("---")

st.header("🛠 Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("Python")

    st.success("Pandas")

    st.success("NumPy")

    st.success("Matplotlib")

with col2:

    st.success("Scikit-Learn")

    st.success("Machine Learning")

    st.success("EDA")

    st.success("Feature Engineering")

with col3:

    st.success("Streamlit")

    st.success("Git")

    st.success("GitHub")

    st.success("Data Visualization")
    st.markdown("---")

st.header("⚙️ Technologies Used")

tech = [
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-Learn",
    "Matplotlib",
    "Plotly",
    "Streamlit",
    "Joblib",
    "GitHub"
]

for item in tech:

    st.write("✅", item)
    st.markdown("---")

st.header("📂 Project Modules")

st.info("""
🌱 Lifestyle Productivity Prediction

💰 Expense Prediction

⚡ Electricity Bill Prediction

📊 Exploratory Data Analysis

📈 Model Comparison

🧠 AI Insights Dashboard
""")
st.markdown("---")

st.header("📊 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric("Datasets", "3")

with c2:

    st.metric("ML Models", "15")

with c3:

    st.metric("Charts", "40+")

with c4:

    st.metric("Modules", "6")
    st.markdown("---")

st.header("🚀 Future Enhancements")

st.write("""
• Deep Learning Integration

• AI Chat Assistant

• User Authentication

• Cloud Database

• Mobile Responsive Dashboard

• PDF Report Generation

• Live Data Integration

• More Prediction Modules
""")
st.markdown("---")

st.header("📬 Contact")

st.write("📧 Email: your_email@example.com")

st.write("💼 LinkedIn: https://www.linkedin.com/in/ananya-yadav-41610229a")

st.write("💻 GitHub: https://github.com/yananya012-svg")
st.markdown("---")

st.success("🎉 LifeSync AI Platform")

st.caption("""
Developed by Ananya Yadav

B.Tech Artificial Intelligence

Python • Machine Learning • Data Science • Streamlit
""")