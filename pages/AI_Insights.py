import streamlit as st

st.set_page_config(
    page_title="AI Insights",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Lifestyle Insights")
st.markdown("---")
st.header("Enter Your Lifestyle Details")

sleep = st.slider("😴 Sleep Hours", 0.0, 12.0, 7.0)

study = st.slider("📚 Study Hours", 0.0, 12.0, 5.0)

exercise = st.slider("💪 Exercise Minutes", 0, 180, 30)

screen = st.slider("📱 Total Screen Time (Hours)", 0.0, 15.0, 5.0)

stress = st.slider("😖 Stress Level", 1, 10, 5)

focus = st.slider("🎯 Focus Score", 1, 100, 60)

score = (
    study * 4 +
    sleep * 5 +
    (exercise / 30) * 5 +
    focus * 0.4 -
    screen * 3 -
    stress * 3
)

score = max(0, min(score, 100))
st.markdown("---")

st.subheader("Overall Lifestyle Score")

st.progress(int(score))

st.metric(
    "Lifestyle Score",
    f"{score:.1f}/100"
)
if score >= 85:
    st.success("🌟 Excellent Lifestyle")

elif score >= 70:
    st.success("😊 Good Lifestyle")

elif score >= 50:
    st.warning("🙂 Average Lifestyle")

else:
    st.error("⚠ Poor Lifestyle")

    st.markdown("---")

st.header("🤖 Personalized AI Recommendations")

if sleep < 7:
    st.warning("😴 Increase sleep to 7–8 hours.")

if study < 5:
    st.info("📚 Increase focused study time.")

if exercise < 30:
    st.warning("💪 Exercise at least 30 minutes.")

if screen > 7:
    st.error("📱 Reduce screen time.")

if stress > 6:
    st.error("🧘 Practice meditation and stress management.")

if focus < 60:
    st.warning("🎯 Improve focus using Pomodoro Technique.")

if (
    sleep >= 7 and
    study >= 5 and
    exercise >= 30 and
    screen <= 5 and
    stress <= 4
):
    st.success("🎉 Excellent routine! Keep it up.")

    st.markdown("---")

st.header("📅 Suggested Daily Routine")

st.table({

    "Activity":[

        "Wake Up",

        "Exercise",

        "Study Session 1",

        "Break",

        "Study Session 2",

        "Entertainment",

        "Sleep"

    ],

    "Suggested Time":[

        "6:30 AM",

        "7:00 AM",

        "9:00 AM",

        "11:00 AM",

        "2:00 PM",

        "6:00 PM",

        "10:30 PM"

    ]

})

st.markdown("---")

st.header("📊 Lifestyle Metrics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("😴 Sleep", f"{sleep} hrs")

with c2:
    st.metric("📚 Study", f"{study} hrs")

with c3:
    st.metric("📱 Screen", f"{screen} hrs")

c4, c5, c6 = st.columns(3)

with c4:
    st.metric("💪 Exercise", f"{exercise} min")

with c5:
    st.metric("😖 Stress", stress)

with c6:
    st.metric("🎯 Focus", focus)

    st.markdown("---")

st.success("""
✅ AI Analysis Completed Successfully

LifeSync AI analyzed your lifestyle and generated personalized recommendations to improve productivity and well-being.
""")

