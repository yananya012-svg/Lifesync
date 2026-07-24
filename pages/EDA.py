import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="EDA Dashboard", page_icon="📊", layout="wide")

st.title("📊 Exploratory Data Analysis Dashboard")

st.markdown("---")

# Load Dataset
df = pd.read_csv("dataset/lifestyle_engineered.csv")

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.markdown("---")

st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

st.markdown("---")

st.header("📈 Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.image("images/productivity_distribution.png",
             caption="Productivity Distribution",
             use_container_width=True)

with col2:
    st.image("images/sleep_distribution.png",
             caption="Sleep Distribution",
             use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/study_vs_productivity.png",
             caption="Study Hours vs Productivity",
             use_container_width=True)

with col2:
    st.image("images/gender_productivity.png",
             caption="Gender Productivity",
             use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/sleep_boxplot.png",
             caption="Sleep Boxplot",
             use_container_width=True)

with col2:
    st.image("images/correlation_heatmap.png",
             caption="Correlation Heatmap",
             use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/exercise_distribution.png",
             caption="Exercise Distribution",
             use_container_width=True)

with col2:
    st.image("images/stress_distribution.png",
             caption="Stress Distribution",
             use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/attendance_distribution.png",
             caption="Attendance Distribution",
             use_container_width=True)

with col2:
    st.image("images/feature_importance.png",
             caption="Feature Importance",
             use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/actual_vs_predicted.png",
             caption="Actual vs Predicted",
             use_container_width=True)

with col2:
    st.image("images/residual_analysis.png",
             caption="Residual Analysis",
             use_container_width=True)

st.markdown("---")

st.success("✅ Exploratory Data Analysis Completed Successfully")