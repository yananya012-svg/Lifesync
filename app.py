import streamlit as st
import os

from auth import register_user, login_user


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="LifeSync AI",
    page_icon="🌱",
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

def load_css():

    try:
        with open("assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except:
        pass


load_css()


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if "user" not in st.session_state:
    st.session_state.user = None



# ==========================================
# LOGIN PAGE
# ==========================================

if not st.session_state.logged_in:


    st.markdown(
        """
        <h1 style="text-align:center;">
        🌱 LifeSync AI
        </h1>

        <h3 style="text-align:center;color:gray;">
        Personal AI Analytics Platform
        </h3>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    login, signup = st.tabs(
        [
            "🔐 Login",
            "📝 Sign Up"
        ]
    )


    # ------------------------------
    # LOGIN
    # ------------------------------

    with login:


        st.subheader("Welcome Back")


        email = st.text_input(
            "Email",
            key="login_email"
        )


        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )


        if st.button(
            "Login",
            use_container_width=True
        ):


            success, user = login_user(
                email,
                password
            )


            if success:

                st.session_state.logged_in = True

                st.session_state.user = user

                st.rerun()


            else:

                st.error(user)



    # ------------------------------
    # SIGN UP
    # ------------------------------

    with signup:


        st.subheader("Create Account")


        name = st.text_input(
            "Full Name"
        )


        email = st.text_input(
            "Email",
            key="signup_email"
        )


        password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )


        confirm = st.text_input(
            "Confirm Password",
            type="password"
        )


        if st.button(
            "Create Account",
            use_container_width=True
        ):


            if password != confirm:

                st.error(
                    "Passwords do not match"
                )


            else:


                success, message = register_user(
                    name,
                    email,
                    password
                )


                if success:

                    st.success(message)

                else:

                    st.error(message)



    st.stop()



# ==========================================
# AFTER LOGIN - PAGE NAVIGATION
# ==========================================


## ==========================================
# PAGE NAVIGATION
# ==========================================

home = st.Page(
    "app_pages/01_🏠_Home.py",
    title="Home",
    icon="🏠"
)

lifestyle = st.Page(
    "app_pages/08_🧠_Lifestyle_Prediction.py",
    title="Lifestyle Prediction",
    icon="🧠"
)

expense = st.Page(
    "app_pages/03_💰_Expense_Prediction.py",
    title="Expense Prediction",
    icon="💰"
)

electricity = st.Page(
    "app_pages/04_⚡_Electricity_Prediction.py",
    title="Electricity Prediction",
    icon="⚡"
)

eda = st.Page(
    "app_pages/02_📊_EDA.py",
    title="EDA",
    icon="📊"
)

model = st.Page(
    "app_pages/05_📈_Model_Comparison.py",
    title="Model Comparison",
    icon="📈"
)

insights = st.Page(
    "app_pages/06_💡_AI_Insights.py",
    title="AI Insights",
    icon="💡"
)

about = st.Page(
    "app_pages/07_👩‍💻_About.py",
    title="About",
    icon="👩‍💻"
)

profile = st.Page(
    "app_pages/09_👤_Profile.py",
    title="Profile",
    icon="👤"
)


navigation = st.navigation(
    [
        home,
        lifestyle,
        expense,
        electricity,
        eda,
        model,
        insights,
        about,
        profile
    ]
)

navigation.run()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:


    st.markdown(
        """
        ## 🌱 LifeSync AI
        
        Personal AI Analytics Platform
        """
    )


    st.divider()


    if st.session_state.user:

        st.success(
            f"👋 {st.session_state.user[1]}"
        )


    st.divider()


    st.subheader("📊 Modules")


    st.write(
        """
        Machine Learning
        Data Analysis
        AI Predictions
        """
    )


    st.divider()


    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.user = None

        st.rerun()



# ==========================================
# RUN NAVIGATION
# ==========================================

navigation = st.navigation(
    [
        home,
        lifestyle,
        expense,
        electricity,
        eda,
        model,
        insights,
        about
    ]
)

navigation.run()