import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Electricity Bill Prediction",
    page_icon="⚡",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


st.title("⚡ Smart Electricity Bill Prediction")

st.write(
    "Predict your monthly electricity bill using Machine Learning."
)

st.markdown("---")

model = joblib.load("models/electricity_model.pkl")
st.subheader("🏠 Enter Household Details")

col1, col2 = st.columns(2)

with col1:

    monthly_units = st.number_input(
        "Monthly Units Consumed",
        min_value=50,
        max_value=1000,
        value=250
    )

    family_members = st.number_input(
        "Family Members",
        min_value=1,
        max_value=10,
        value=4
    )

    rooms = st.number_input(
        "Number of Rooms",
        min_value=1,
        max_value=10,
        value=3
    )

    ac_count = st.number_input(
        "Number of ACs",
        min_value=0,
        max_value=5,
        value=1
    )

with col2:

    refrigerator = st.selectbox(
        "Refrigerator",
        [0,1]
    )

    washing_machine = st.selectbox(
        "Washing Machine",
        [0,1]
    )

    geyser = st.selectbox(
        "Geyser",
        [0,1]
    )

    laptop_count = st.number_input(
        "Laptop Count",
        min_value=0,
        max_value=10,
        value=2
    )

    tv_count = st.number_input(
        "TV Count",
        min_value=0,
        max_value=5,
        value=1
    )

house_type = st.selectbox(

    "House Type",

    [

        "Apartment",

        "Independent House",

        "Villa"

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

work_from_home = st.selectbox(

    "Work From Home",

    [

        "No",

        "Yes"

    ]

)

solar_panel = st.selectbox(

    "Solar Panel Installed",

    [

        "No",

        "Yes"

    ]

)
house_map = {

    "Apartment":0,

    "Independent House":1,

    "Villa":2

}

city_map = {

    "Tier_1":0,

    "Tier_2":1,

    "Tier_3":2

}

yes_no = {

    "No":0,

    "Yes":1

}
if st.button(
    "⚡ Predict Electricity Bill",
    key="electricity_prediction"
):
    

    total_appliances = (
        ac_count
        + refrigerator
        + washing_machine
        + geyser
        + laptop_count
        + tv_count
    )

    units_per_member = (
        monthly_units / family_members
    )

    room_density = (
        family_members / rooms
    )

    bill_per_unit = 8.0

    energy_score = max(
        0,
        100 - (bill_per_unit * 10) - (ac_count * 2)
    )

    if monthly_units < 200:
        category = 0

    elif monthly_units < 400:
        category = 1

    elif monthly_units < 600:
        category = 2

    else:
        category = 3
            # ---------------------------------------
    # Prepare Input Data
    # ---------------------------------------

    input_df = pd.DataFrame({

        "monthly_units": [monthly_units],

        "house_type": [house_map[house_type]],

        "city": [city_map[city]],

        "family_members": [family_members],

        "rooms": [rooms],

        "ac_count": [ac_count],

        "refrigerator": [refrigerator],

        "washing_machine": [washing_machine],

        "geyser": [geyser],

        "laptop_count": [laptop_count],

        "tv_count": [tv_count],

        "work_from_home": [yes_no[work_from_home]],

        "solar_panel": [yes_no[solar_panel]],

        "total_appliances": [total_appliances],

        "units_per_member": [units_per_member],

        "bill_per_unit": [bill_per_unit],

        "room_density": [room_density],

        "consumption_category": [category],

        "energy_efficiency_score": [energy_score]

    })

    # ---------------------------------------
    # Predict Electricity Bill
    # ---------------------------------------

    prediction = model.predict(input_df)[0]

    st.success(
        f"⚡ Estimated Monthly Electricity Bill: ₹ {prediction:,.2f}"
    )
    

    # ---------------------------------------
    # Summary Cards
    # ---------------------------------------

    st.markdown("---")

    st.subheader("📊 Electricity Bill Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "⚡ Monthly Units",
            monthly_units
        )

    with col2:
        st.metric(
            "💰 Estimated Bill",
            f"₹ {prediction:,.0f}"
        )

    with col3:
        st.metric(
            "🌱 Energy Score",
            f"{energy_score:.0f}/100"
        )
            # ---------------------------------------
    # Energy Efficiency Progress
    # ---------------------------------------

    st.markdown("---")

    st.subheader("⚡ Energy Efficiency")

    st.progress(energy_score / 100)

    st.write(
        f"Your home's Energy Efficiency Score is **{energy_score:.0f}/100**."
    )

    if energy_score >= 80:

        st.success("🟢 Excellent Energy Efficiency")

    elif energy_score >= 60:

        st.info("🟡 Good Energy Efficiency")

    elif energy_score >= 40:

        st.warning("🟠 Average Energy Efficiency")

    else:

        st.error("🔴 Poor Energy Efficiency")
            # ---------------------------------------
    # Electricity Usage Gauge
    # ---------------------------------------

    st.markdown("---")

    st.subheader("⚡ Monthly Electricity Usage")

    usage = min((monthly_units / 1000) * 100, 100)

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=usage,

            title={"text":"Electricity Usage (%)"},

            gauge={

                "axis":{"range":[0,100]},

                "steps":[

                    {"range":[0,40],"color":"lightgreen"},

                    {"range":[40,70],"color":"yellow"},

                    {"range":[70,100],"color":"red"}

                ]

            }

        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
        # ---------------------------------------
    # Appliance Distribution
    # ---------------------------------------

    st.markdown("---")

    st.subheader("🥧 Appliance Distribution")

    pie = pd.DataFrame({

        "Appliance":[

            "AC",

            "Refrigerator",

            "Washing Machine",

            "Geyser",

            "Laptop",

            "TV"

        ],

        "Count":[

            ac_count,

            refrigerator,

            washing_machine,

            geyser,

            laptop_count,

            tv_count

        ]

    })

    fig = px.pie(

        pie,

        names="Appliance",

        values="Count",

        title="Household Appliance Usage"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
        # ---------------------------------------
    # Household Statistics
    # ---------------------------------------

    st.markdown("---")

    st.subheader("📊 Household Statistics")

    bar = pd.DataFrame({

        "Category":[

            "Units",

            "Rooms",

            "Family",

            "Appliances"

        ],

        "Value":[

            monthly_units,

            rooms,

            family_members,

            total_appliances

        ]

    })

    fig = px.bar(

        bar,

        x="Category",

        y="Value",

        title="Household Overview"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
        # ---------------------------------------
    # AI Recommendations
    # ---------------------------------------

    st.markdown("---")

    st.subheader("💡 AI Electricity Saving Tips")

    if monthly_units < 250:

        st.success("""

        ✅ Excellent electricity management.

        Recommendations:

        • Continue your current usage.

        • Switch off unused appliances.

        • Continue using LED bulbs.

        """)

    elif monthly_units < 500:

        st.warning("""

        ⚠ Moderate electricity usage.

        Recommendations:

        • Reduce AC usage.

        • Use appliances during off-peak hours.

        • Upgrade to energy-efficient appliances.

        """)

    else:

        st.error("""

        🚨 High electricity consumption.

        Recommendations:

        • Install rooftop solar panels.

        • Replace old appliances.

        • Reduce unnecessary electricity usage.

        • Monitor your monthly consumption.

        """)
        
    # ---------------------------------------
    # Download Report
    # ---------------------------------------

    st.markdown("---")

    st.subheader("📥 Download Electricity Report")

    report = pd.DataFrame({

        "Monthly Units":[monthly_units],

        "Predicted Bill":[prediction],

        "Energy Score":[energy_score],

        "House Type":[house_type],

        "City":[city],

        "Family Members":[family_members]

    })

    csv = report.to_csv(index=False)

    st.download_button(

        label="⬇ Download Electricity Report",

        data=csv,

        file_name="Electricity_Report.csv",

        mime="text/csv",

        key="electricity_report"

    )

    st.success("🎉 Electricity Bill Prediction Completed Successfully!")