import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
import time
import random


# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="LifeSync AI",
    page_icon="🌱",
    layout="wide"
)


# ==============================
# CSS
# ==============================

try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass



# ==============================
# LOAD MODEL
# ==============================

model = joblib.load(
    "models/lifesync_model.pkl"
)



# ==============================
# HEADER
# ==============================

st.title("🌱 LifeSync AI")

st.subheader(
    "AI Powered Productivity Prediction Dashboard"
)

st.divider()


st.info(
    "Enter your lifestyle details and get AI productivity insights."
)



# ==============================
# INPUT SECTION
# ==============================

st.header("📝 Daily Lifestyle Information")


col1,col2 = st.columns(2)



with col1:


    age = st.slider(
        "Age",
        17,
        30,
        22
    )


    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


    study_hours = st.slider(
        "📚 Study Hours",
        0.0,
        12.0,
        5.0
    )


    sleep_hours = st.slider(
        "😴 Sleep Hours",
        3.0,
        12.0,
        7.0
    )


    phone_usage = st.slider(
        "📱 Phone Usage Hours",
        0.0,
        15.0,
        4.0
    )


    social_media = st.slider(
        "📵 Social Media Hours",
        0.0,
        10.0,
        2.0
    )



with col2:


    youtube = st.slider(
        "▶️ YouTube Hours",
        0.0,
        10.0,
        1.0
    )


    gaming = st.slider(
        "🎮 Gaming Hours",
        0.0,
        10.0,
        1.0
    )


    breaks = st.slider(
        "☕ Breaks Per Day",
        0,
        20,
        5
    )


    coffee = st.slider(
        "☕ Coffee Intake (mg)",
        0,
        500,
        150
    )


    exercise = st.slider(
        "🏃 Exercise Minutes",
        0,
        180,
        30
    )


    assignments = st.slider(
        "📖 Assignments Completed",
        0,
        20,
        5
    )



attendance = st.slider(
    "🏫 Attendance %",
    0.0,
    100.0,
    85.0
)


stress = st.slider(
    "😰 Stress Level",
    1,
    10,
    5
)


focus = st.slider(
    "🎯 Focus Score",
    1,
    100,
    70
)
# ==============================
# PREDICTION BUTTON
# ==============================


if st.button(
    "🚀 Predict Productivity",
    use_container_width=True
):


    with st.spinner(
        "🤖 AI analyzing your lifestyle..."
    ):


        time.sleep(1)



        # Derived Features


        total_screen_time = (
            phone_usage
            +
            social_media
            +
            youtube
            +
            gaming
        )



        if sleep_hours >= 8:

            sleep_quality = 2

        elif sleep_hours >=6:

            sleep_quality = 1

        else:

            sleep_quality = 0



        if exercise >=45:

            exercise_level = 2

        elif exercise >=20:

            exercise_level = 1

        else:

            exercise_level = 0




        if stress <=3:

            stress_category = 0

        elif stress <=7:

            stress_category = 1

        else:

            stress_category = 2



        focus_efficiency = (
            focus /
            (study_hours + 1)
        )



        lifestyle_balance_score = (

            sleep_hours
            +
            exercise/10
            +
            attendance/10
            -
            stress

        )



        gender_value = 1 if gender=="Male" else 0



        # MODEL INPUT

        input_data = pd.DataFrame({

            "age":[age],

            "gender":[gender_value],

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

            "total_screen_time":[total_screen_time],

            "sleep_quality":[sleep_quality],

            "exercise_level":[exercise_level],

            "stress_category":[stress_category],

            "focus_efficiency":[focus_efficiency],

            "lifestyle_balance_score":[lifestyle_balance_score]

        })



        prediction = model.predict(
            input_data
        )[0]



        prediction = max(
            0,
            min(100,prediction)
        )



    st.success(
        "✅ AI Analysis Completed"
    )


    st.metric(
        "🌱 Productivity Score",
        f"{prediction:.2f}%"
    )
    st.divider()



    # Category

    if prediction >=80:

        st.success(
            "🏆 Excellent Productivity"
        )


    elif prediction >=60:

        st.info(
            "🥇 Good Productivity"
        )


    else:

        st.warning(
            "⚠ Needs Improvement"
        )



    # Gauge Chart


    gauge = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=prediction,

            title={
                "text":"Productivity Score"
            },

            gauge={
                "axis":{
                    "range":[0,100]
                }
            }

        )
    )



    st.plotly_chart(
        gauge,
        use_container_width=True
    )



    # Pie Chart


    chart = pd.DataFrame({

        "Activity":[

            "Study",
            "Phone",
            "Social Media",
            "Gaming",
            "Sleep"

        ],

        "Hours":[

            study_hours,
            phone_usage,
            social_media,
            gaming,
            sleep_hours

        ]

    })


    fig = px.pie(

        chart,

        names="Activity",

        values="Hours"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    # Recommendations


    st.subheader(
        "🧠 AI Recommendations"
    )


    if phone_usage >5:

        st.warning(
            "Reduce phone usage."
        )


    if exercise <30:

        st.warning(
            "Increase daily exercise."
        )


    if sleep_hours <6:

        st.warning(
            "Improve sleep schedule."
        )


    if stress >7:

        st.warning(
            "Practice stress management."
        )


    if phone_usage<=5 and exercise>=30:

        st.success(
            "Great lifestyle balance!"
        )



    # Download Report


    report = pd.DataFrame({

        "Productivity":[prediction],

        "Study Hours":[study_hours],

        "Sleep Hours":[sleep_hours],

        "Exercise Minutes":[exercise],

        "Stress":[stress]

    })



    st.download_button(

        "📥 Download Report",

        report.to_csv(index=False),

        "LifeSync_Report.csv",

        "text/csv"

    )


    st.success(
        "🎉 Prediction Completed Successfully!"
    )



st.divider()


st.info(
    f"💡 AI Quote: {random.choice([
        'Consistency creates success.',
        'Healthy habits build productivity.',
        'Small improvements create big results.'
    ])}"
)