import streamlit as st

from database import get_history


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)


# =====================================
# LOGIN CHECK
# =====================================

if not st.session_state.get(
    "logged_in",
    False
):

    st.warning(
        "Please login first."
    )

    st.stop()



# =====================================
# USER DATA
# =====================================

user = st.session_state.user



# =====================================
# PROFILE HEADER
# =====================================

st.title("👤 My Profile")


st.success(
    f"Welcome, {user[1]} 👋"
)


st.divider()



# =====================================
# USER DETAILS
# =====================================

st.subheader(
    "Personal Information"
)


col1, col2 = st.columns(2)


with col1:

    st.info(
        f"""
        👤 Name

        {user[1]}
        """
    )


with col2:

    st.info(
        f"""
        📧 Email

        {user[2]}
        """
    )



st.divider()



# =====================================
# PREDICTION HISTORY
# =====================================

st.subheader(
    "📜 Prediction History"
)



history = get_history(
    user[0]
)



if history:


    for item in history:

        st.success(
            f"""
            🔹 Prediction Type: {item[0]}

            📊 Result: {item[1]}

            📅 Date: {item[2]}
            """
        )


else:


    st.info(
        "No predictions available yet."
    )



st.divider()



st.subheader(
    "📊 Account Status"
)


st.success(
    "🟢 Active User"
)
st.metric(
    "Account Status",
    "Active"
)

st.metric(
    "Predictions Made",
    len(history)
)