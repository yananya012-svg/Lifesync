import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="LifeSync AI - Productivity Prediction",
    page_icon="🌱",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================================
# Load Model
# ==========================================

model = joblib.load("models/lifesync_model.pkl")

# ==========================================
# Header
# ==========================================

st.title("🌱 LifeSync AI")
st.subheader("AI Powered Productivity Prediction Dashboard")

st.markdown("---")

st.info(
    "Enter your daily lifestyle details and get AI-powered productivity insights."
)

# ==========================================
# Input Section
# ==========================================

st.header("📝 Daily Lifestyle Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider("Age", 17, 30, 22)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    study_hours = st.slider(
        "📚 Study Hours",
        0.0, 12.0, 5.0
    )

    sleep_hours = st.slider(
        "😴 Sleep Hours",
        3.0, 12.0, 7.5
    )

    phone_usage = st.slider(
        "📱 Phone Usage (Hours)",
        0.0, 15.0, 4.0
    )

    social_media = st.slider(
        "📵 Social Media Hours",
        0.0, 10.0, 2.0
    )

with col2:

    youtube = st.slider(
        "▶️ YouTube Hours",
        0.0, 10.0, 1.5
    )

    gaming = st.slider(
        "🎮 Gaming Hours",
        0.0, 10.0, 1.0
    )

    breaks = st.slider(
        "☕ Breaks Per Day",
        0, 20, 5
    )

    coffee = st.slider(
        "☕ Coffee Intake (mg)",
        0, 500, 150
    )

    exercise = st.slider(
        "🏃 Exercise Minutes",
        0, 180, 30
    )

    assignments = st.slider(
        "📖 Assignments Completed",
        0, 20, 5
    )

attendance = st.slider(
    "🏫 Attendance (%)",
    0.0, 100.0, 85.0
)

stress = st.slider(
    "😰 Stress Level",
    1, 10, 5
)

focus = st.slider(
    "🎯 Focus Score",
    1, 100, 70
)

# ==========================================
# Predict Button
# ==========================================

if st.button(
    "🚀 Predict Productivity",
    use_container_width=True
):

    # Derived Features

    total_screen = phone_usage + social_media + youtube + gaming

    focus_efficiency = (
        focus / (study_hours + 1)
    )

    lifestyle_balance = (
        sleep_hours * 2
        + exercise / 30
        - stress
        - total_screen
    )

    # Encode Categories

    gender_val = 1 if gender == "Male" else 0

    if sleep_hours >= 7:
        sleep_quality = 0
    elif sleep_hours >= 5:
        sleep_quality = 1
    else:
        sleep_quality = 2

    if exercise >= 60:
        exercise_level = 0
    elif exercise >= 20:
        exercise_level = 1
    else:
        exercise_level = 2

    if stress >= 7:
        stress_category = 0
    elif stress >= 4:
        stress_category = 1
    else:
        stress_category = 2

    # Create Input DataFrame

    input_data = pd.DataFrame({

        "age":[age],
        "gender":[gender_val],
        "study_hours_per_day":[study_hours],
        "sleep_hours":[sleep_hours],
        "phone_usage_hours":[phone_usage],
        "social_media_hours":[social_media],
        "youtube_hours":[youtube],
        "gaming_hours":[gaming],
        "breaks_per_day":[breaks],
        "coffee_intake_mg":[coffee],
        "exercise_minutes":[exercise],
        "assignments_completed":[assignments],
        "attendance_percentage":[attendance],
        "stress_level":[stress],
        "focus_score":[focus],
        "total_screen_time":[total_screen],
        "sleep_quality":[sleep_quality],
        "exercise_level":[exercise_level],
        "stress_category":[stress_category],
        "focus_efficiency":[focus_efficiency],
        "lifestyle_balance_score":[lifestyle_balance]

    })

    # Prediction

    prediction = model.predict(input_data)[0]
    prediction = max(0, min(100, prediction))

    # ==========================================
    # Result Header
    # ==========================================

    st.markdown("---")

    if prediction >= 80:
        st.success("🏆 Excellent Productivity")

    elif prediction >= 60:
        st.info("🥇 Good Productivity")

    elif prediction >= 40:
        st.warning("🥈 Moderate Productivity")

    else:
        st.error("🥉 Needs Improvement")

    # ==========================================
    # KPI Cards
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📈 Productivity",
            f"{prediction:.1f}%"
        )

    with c2:
        st.metric(
            "🎯 Focus",
            focus
        )

    with c3:
        st.metric(
            "😰 Stress",
            stress
        )

    with c4:
        st.metric(
            "😴 Sleep",
            f"{sleep_hours:.1f} hrs"
        )

    # ==========================================
    # Gauge Chart
    # ==========================================

    st.markdown("---")

    st.subheader("⚡ Productivity Gauge")

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=prediction,

        title={"text":"Productivity Score"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"green"},

            "steps":[

                {"range":[0,40],"color":"#ffcccc"},

                {"range":[40,70],"color":"#ffe5b4"},

                {"range":[70,100],"color":"#ccffcc"}

            ]

        }

    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # Charts Section
    # ==========================================

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🥧 Daily Time Usage")

        pie = px.pie(

            names=[
                "Study",
                "Phone",
                "Social Media",
                "YouTube",
                "Gaming",
                "Sleep"
            ],

            values=[
                study_hours,
                phone_usage,
                social_media,
                youtube,
                gaming,
                sleep_hours
            ]

        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    with col2:

        st.subheader("📊 Lifestyle Comparison")

        bar = px.bar(

            x=[
                "Study",
                "Sleep",
                "Phone",
                "Exercise"
            ],

            y=[
                study_hours,
                sleep_hours,
                phone_usage,
                exercise / 10
            ]

        )

        st.plotly_chart(
            bar,
            use_container_width=True
        )

    # ==========================================
    # AI Recommendations
    # ==========================================

    st.markdown("---")

    st.subheader("🧠 Personalized AI Recommendations")

    recommendations = []

    if study_hours < 6:
        recommendations.append(
            "📚 Increase study time to 6–8 hours for better productivity."
        )

    if phone_usage > 5:
        recommendations.append(
            "📱 Reduce phone usage to less than 5 hours."
        )

    if social_media > 3:
        recommendations.append(
            "📵 Limit social media usage to improve concentration."
        )

    if exercise < 30:
        recommendations.append(
            "🏃 Exercise for at least 30 minutes daily."
        )

    if attendance < 75:
        recommendations.append(
            "🏫 Improve attendance above 75%."
        )

    if focus < 60:
        recommendations.append(
            "🎯 Use Pomodoro technique to improve focus."
        )

    if stress > 7:
        recommendations.append(
            "🧘 Practice meditation and reduce workload."
        )

    if len(recommendations) == 0:

        st.success(
            "🎉 Excellent lifestyle balance! Keep maintaining these habits."
        )

    else:

        for rec in recommendations:
            st.write("•", rec)

    # ==========================================
    # Wellness Score
    # ==========================================

    st.markdown("---")

    wellness = (

        prediction * 0.4 +

        focus * 0.3 +

        attendance * 0.2 +

        (100 - stress * 10) * 0.1

    )

    st.subheader("💚 Overall Wellness Score")

    st.metric(
        "Wellness Score",
        f"{wellness:.1f}/100"
    )

    st.progress(wellness / 100)

    # ==========================================
    # Download Report
    # ==========================================

    st.markdown("---")

    report = pd.DataFrame({

        "Productivity Score":[round(prediction,2)],
        "Wellness Score":[round(wellness,2)],
        "Study Hours":[study_hours],
        "Sleep Hours":[sleep_hours],
        "Phone Usage":[phone_usage],
        "Exercise Minutes":[exercise]

    })

    csv = report.to_csv(index=False)

    st.download_button(

        label="📥 Download Productivity Report",

        data=csv,

        file_name="LifeSync_Productivity_Report.csv",

        mime="text/csv"

    )

    st.success(
        "🎉 Prediction Completed Successfully!"
    )