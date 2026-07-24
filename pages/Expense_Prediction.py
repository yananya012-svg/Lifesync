import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(
    page_title="Expense Prediction",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Smart Monthly Expense Prediction")
st.write("Predict your monthly expenses using Machine Learning.")

st.markdown("---")
model = joblib.load("models/expense_model.pkl")

# -----------------------------------
# User Inputs
# -----------------------------------

st.subheader("📝 Enter Your Details")

col1, col2 = st.columns(2)

with col1:

    income = st.number_input(
        "Monthly Income (₹)",
        min_value=10000,
        max_value=500000,
        value=50000,
        step=1000
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=25
    )

    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=10,
        value=1
    )

with col2:

    occupation = st.selectbox(
        "Occupation",
        [
            "Professional",
            "Retired",
            "Self_Employed",
            "Student"
        ]
    )

    city = st.selectbox(
        "City Tier",
        [
            "Tier_1",
            "Tier_2",
            "Tier_3"
        ]
    )

    saving = st.slider(
        "Desired Savings Percentage (%)",
        min_value=0,
        max_value=100,
        value=20
    )

    # -----------------------------------
# Encode Inputs
# -----------------------------------

occupation_map = {

    "Professional":0,
    "Retired":1,
    "Self_Employed":2,
    "Student":3

}

city_map = {

    "Tier_1":0,
    "Tier_2":1,
    "Tier_3":2

}
# -----------------------------------
# Prediction Button
# -----------------------------------

if st.button("💰 Predict Expense", key="predict_expense_button"):

    input_df = pd.DataFrame({

        "Income":[income],
        "Age":[age],
        "Dependents":[dependents],
        "Occupation":[occupation_map[occupation]],
        "City_Tier":[city_map[city]],
        "Desired_Savings_Percentage":[saving]

    })

    prediction = model.predict(input_df)[0]

    savings = income - prediction

    expense_ratio = (prediction / income) * 100

    st.success(
        f"💰 Estimated Monthly Expense: ₹ {prediction:,.2f}"
    )
        # -----------------------------------
    # Financial Recommendation
    # -----------------------------------

    if prediction < income * 0.5:
            st.success("✅ Excellent Financial Management")

    elif prediction < income * 0.8:
            st.warning("⚠️ Your spending is moderate.")

    else:
            st.error("🚨 Your expenses are quite high.")

        # -----------------------------------
        # Financial Summary
        # -----------------------------------

    st.markdown("---")

    st.subheader("📊 Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
            st.metric(
                "💵 Income",
                f"₹ {income:,.0f}"
            )

    with col2:
            st.metric(
                "💸 Predicted Expense",
                f"₹ {prediction:,.0f}"
            )

    with col3:
            st.metric(
                "💰 Remaining Savings",
                f"₹ {savings:,.0f}"
            )

        # -----------------------------------
        # Expense Ratio
        # -----------------------------------

    st.markdown("---")

    st.subheader("💰 Expense Ratio")

    st.progress(expense_ratio / 100)

    st.write(
            f"You spend **{expense_ratio:.2f}%** of your monthly income."
        )
        # ---------------------------------------
    # Financial Health Score
    # ---------------------------------------

    financial_score = max(0, 100 - expense_ratio)

    st.markdown("---")

    st.subheader("🎯 Financial Health Score")

    st.metric(
        "Overall Score",
        f"{financial_score:.0f}/100"
    )

    if financial_score >= 80:
        st.success("🟢 Excellent Financial Health")

    elif financial_score >= 60:
        st.info("🟡 Good Financial Health")

    elif financial_score >= 40:
        st.warning("🟠 Average Financial Health")

    else:
        st.error("🔴 Poor Financial Health")


    # ---------------------------------------
    # Budget Category
    # ---------------------------------------

    st.markdown("---")

    st.subheader("🏆 Budget Category")

    if expense_ratio < 50:
        st.success("🏆 Excellent Budget Management")

    elif expense_ratio < 70:
        st.info("🥇 Good Budget Management")

    elif expense_ratio < 85:
        st.warning("🥈 Moderate Budget Management")

    else:
        st.error("🥉 Poor Budget Management")


    # ---------------------------------------
    # Expense vs Savings Pie Chart
    # ---------------------------------------

    st.markdown("---")

    st.subheader("📈 Expense vs Savings")

    pie_data = pd.DataFrame({

        "Category": ["Expense", "Savings"],

        "Amount": [prediction, savings]

    })

    fig = px.pie(

        pie_data,

        names="Category",

        values="Amount",

        title="Expense Distribution"

    )

    st.plotly_chart(fig, use_container_width=True)


    # ---------------------------------------
    # Income vs Expense vs Savings
    # ---------------------------------------

    st.markdown("---")

    st.subheader("📊 Financial Comparison")

    bar_data = pd.DataFrame({

        "Category": ["Income", "Expense", "Savings"],

        "Amount": [income, prediction, savings]

    })

    fig = px.bar(

        bar_data,

        x="Category",

        y="Amount",

        title="Income vs Expense vs Savings"

    )

    st.plotly_chart(fig, use_container_width=True)


    # ---------------------------------------
    # Expense Ratio Gauge
    # ---------------------------------------

    st.markdown("---")

    st.subheader("💰 Expense Ratio Gauge")

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=expense_ratio,

            title={"text": "Expense Ratio (%)"},

            gauge={

                "axis": {"range": [0, 100]},

                "steps": [

                    {"range": [0, 50], "color": "lightgreen"},

                    {"range": [50, 80], "color": "yellow"},

                    {"range": [80, 100], "color": "red"}

                ]

            }

        )

    )

    st.plotly_chart(fig, use_container_width=True)


    # ---------------------------------------
    # Personalized Saving Tips
    # ---------------------------------------

    st.markdown("---")

    st.subheader("💡 Personalized Saving Tips")

    if income < 30000:

        st.info("""

        • Focus on essential expenses.

        • Save at least 10% every month.

        • Avoid unnecessary subscriptions.

        """)

    elif income < 70000:

        st.success("""

        • Maintain an emergency fund.

        • Invest regularly.

        • Track monthly spending.

        """)

    else:

        st.success("""

        • Increase long-term investments.

        • Diversify your portfolio.

        • Build passive income sources.

        """)


    # ---------------------------------------
    # Download Report
    # ---------------------------------------

    st.markdown("---")

    st.subheader("📥 Download Expense Report")

    report = pd.DataFrame({

        "Income": [income],

        "Predicted Expense": [prediction],

        "Savings": [savings],

        "Expense Ratio (%)": [round(expense_ratio, 2)],

        "Financial Score": [round(financial_score, 0)]

    })

    csv = report.to_csv(index=False)

    st.download_button(

        label="⬇️ Download Report",

        data=csv,

        file_name="Expense_Report.csv",

        mime="text/csv",

        key="download_expense_report"

    )

    st.success("🎉 Prediction Completed Successfully!")

        