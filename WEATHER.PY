import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import(MinMaxScaler,StandardScaler)
from tensorflow.keras.models import Model
from tensorflow.keras.layers import(Input,LTSM,Dense,dropout)
from tensorflow.keras.utils import to_categprical

## PAGE OVERVIEW ##
st.set_page_config(
    page_title="AI Weather Forecasting",
    page_icon="🌦️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
    color:white;
}

h1,h2,h3,h4,h5,p,label{
    color:white !important;
}

.block{
    background:rgba(255,255,255,0.12);
    padding:25px;
    border-radius:20px;
    margin-bottom:20px;
    backdrop-filter: blur(10px);
}

.metric-card{
    background:rgba(255,255,255,0.14);
    padding:20px;
    border-radius:20px;
    text-align:center;
}

.forecast-card{
    background:rgba(255,255,255,0.12);
    padding:20px;
    border-radius:20px;
    text-align:center;
}

.big-temp{
    font-size:70px;
    font-weight:bold;
}

.condition{
    font-size:24px;
    color:#dbeafe;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<h1 style='text-align:center;'>
🌦️ AI Weather Forecasting Dashboard
</h1>

<p style='text-align:center;font-size:18px;'>
LSTM Based Temperature & Weather Prediction System
</p>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Forecast Settings")

future_days = st.sidebar.slider(
    "Forecast Days",
    1,
    14,
    7
)

city = st.sidebar.text_input(
    "City Name",
    "Delhi"
)

forecast_btn = st.sidebar.button(
    "Generate Forecast"
)

# =========================================================
# LOAD CSV DATASET
# =========================================================

# IMPORTANT:
# Make sure Weather_report.csv exists
# in same folder as app.py

df = pd.read_csv("Weather_report.csv")

# =========================================================
# DISPLAY DATASET
# =========================================================

st.subheader("📂 Weather Dataset")

st.dataframe(
    df.head(),
    use_container_width=True
)

# =========================================================
# COLUMN HANDLING
# =========================================================

# Change these column names according
# to your CSV dataset

# Example CSV Columns:
# Date
# Temperature
# Humidity
# Condition

# =========================================================

# Convert date column


df=pd.read_csv(r'Weather_report.csv')

# =========================================
# Display Content
# =========================================

