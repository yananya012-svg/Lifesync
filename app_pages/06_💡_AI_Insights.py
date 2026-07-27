import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="AI Insights",
    page_icon="🧠",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("🧠 AI Insights Dashboard")

st.write(
    "Overall AI analysis of Lifestyle, Finance and Energy."
)

st.markdown("---")
st.header("🏆 Overall AI Scores")

col1, col2, col3, col4 = st.columns(4)

with col1:

    lifestyle_score = 85

    st.metric(
        "🌱 Lifestyle",
        f"{lifestyle_score}/100"
    )

with col2:

    finance_score = 78

    st.metric(
        "💰 Finance",
        f"{finance_score}/100"
    )

with col3:

    energy_score = 88

    st.metric(
        "⚡ Energy",
        f"{energy_score}/100"
    )

with col4:

    overall = round(
        (lifestyle_score + finance_score + energy_score) / 3
    )

    st.metric(
        "🧠 Overall",
        f"{overall}/100"
    )

st.markdown("---")
st.header("📊 AI Performance")

st.write("Lifestyle Score")

st.progress(lifestyle_score / 100)

st.write("Financial Health")

st.progress(finance_score / 100)

st.write("Energy Efficiency")

st.progress(energy_score / 100)

st.write("Overall Wellness")

st.progress(overall / 100)

st.markdown("---")
st.header("📈 Overall Performance Radar")

categories = [

    "Lifestyle",

    "Finance",

    "Energy"

]

fig = go.Figure()

fig.add_trace(

    go.Scatterpolar(

        r=[
            lifestyle_score,
            finance_score,
            energy_score
        ],

        theta=categories,

        fill="toself",

        name="AI Scores"

    )

)

fig.update_layout(

    polar=dict(

        radialaxis=dict(

            visible=True,

            range=[0,100]

        )

    ),

    showlegend=False

)

st.plotly_chart(
    fig,
    use_container_width=True
)
# ----------------------------------------
# AI Recommendations
# ----------------------------------------

st.markdown("---")

st.header("💡 Personalized AI Recommendations")

# Lifestyle

if lifestyle_score >= 80:

    st.success("""
🌱 Lifestyle Analysis

✅ Excellent lifestyle habits.

Recommendations:

• Maintain your study schedule.

• Continue exercising regularly.

• Keep your sleep routine consistent.

• Stay hydrated.
""")

elif lifestyle_score >= 60:

    st.warning("""
🌱 Lifestyle Analysis

⚠ Lifestyle is good but can improve.

Recommendations:

• Sleep at least 7–8 hours.

• Reduce screen time.

• Increase physical activity.
""")

else:

    st.error("""
🌱 Lifestyle Analysis

🚨 Lifestyle needs improvement.

Recommendations:

• Maintain a fixed daily routine.

• Exercise regularly.

• Reduce stress.

• Improve sleep quality.
""")

# Finance

if finance_score >= 80:

    st.success("""
💰 Financial Analysis

Excellent financial management.

Recommendations:

• Continue saving regularly.

• Invest wisely.

• Maintain your monthly budget.
""")

elif finance_score >= 60:

    st.warning("""
💰 Financial Analysis

Moderate spending detected.

Recommendations:

• Reduce unnecessary purchases.

• Increase monthly savings.

• Track expenses weekly.
""")

else:

    st.error("""
💰 Financial Analysis

High financial risk detected.

Recommendations:

• Create a strict monthly budget.

• Reduce entertainment expenses.

• Avoid unnecessary shopping.
""")

# Energy

if energy_score >= 80:

    st.success("""
⚡ Energy Analysis

Excellent energy efficiency.

Recommendations:

• Continue using energy-efficient appliances.

• Switch off unused devices.

• Consider solar energy.
""")

elif energy_score >= 60:

    st.warning("""
⚡ Energy Analysis

Moderate electricity consumption.

Recommendations:

• Reduce AC usage.

• Use LED bulbs.

• Monitor electricity bills.
""")

else:

    st.error("""
⚡ Energy Analysis

High electricity usage detected.

Recommendations:

• Reduce appliance usage.

• Replace old appliances.

• Install solar panels if possible.
""")
    # ----------------------------------------
# Wellness Badge
# ----------------------------------------

st.markdown("---")

st.header("🏅 Overall Wellness Badge")

if overall >= 90:

    st.success("🥇 Platinum Wellness")

elif overall >= 80:

    st.success("🥈 Gold Wellness")

elif overall >= 70:

    st.info("🥉 Silver Wellness")

elif overall >= 60:

    st.warning("🟡 Bronze Wellness")

else:

    st.error("🔴 Needs Improvement")
    # ----------------------------------------
# Score Summary
# ----------------------------------------

st.markdown("---")

st.header("📊 AI Score Summary")

summary = pd.DataFrame({

    "Category":[

        "Lifestyle",

        "Finance",

        "Energy",

        "Overall"

    ],

    "Score":[

        lifestyle_score,

        finance_score,

        energy_score,

        overall

    ]

})

st.dataframe(
    summary,
    use_container_width=True
)
# ----------------------------------------
# Download AI Report
# ----------------------------------------

st.markdown("---")

st.header("📥 Download AI Report")

csv = summary.to_csv(index=False)

st.download_button(

    label="⬇ Download AI Report",

    data=csv,

    file_name="LifeSync_AI_Report.csv",

    mime="text/csv",

    key="download_ai_report"

)
# ----------------------------------------
# Dashboard Highlights
# ----------------------------------------

st.markdown("---")

st.header("✨ Dashboard Highlights")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 🤖 Artificial Intelligence

✔ Lifestyle Prediction

✔ Expense Prediction

✔ Electricity Prediction

✔ Personalized Recommendations

✔ Interactive Dashboards
""")

with col2:

    st.info("""
### 📊 Analytics

✔ Machine Learning

✔ Model Comparison

✔ Professional Charts

✔ Download Reports

✔ AI Insights
""")
    # ----------------------------------------
# Footer
# ----------------------------------------

st.markdown("---")

st.success("🎉 AI Insights Dashboard Completed Successfully!")

st.caption("""

🌱 LifeSync AI

Developed by Ananya Yadav

B.Tech Artificial Intelligence

Python • Machine Learning • Streamlit • Data Science

""")

