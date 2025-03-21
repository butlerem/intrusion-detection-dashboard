import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import requests
import numpy as np

#######################
# Page Configuration
st.set_page_config(
    page_title="Intrusion Detection Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

#######################
# Load Intrusion Detection Data
df_intrusions = pd.read_csv('data/cybersecurity_intrusions.csv')

#######################
# Sidebar Filters
with st.sidebar:
    st.title('🛡️ Intrusion Detection Dashboard')

    st.markdown("### This app predicts whether a network session is likely to be a cyberattack based on session characteristics such as packet size, login attemps, and IP reputation. Powered by a LightGBM model trained on labeled intrusion data.")
    
    st.markdown("### Model Info")
    st.markdown("""
    - **Model:** LightGBM Classifier  
    - **Recall:** 87.1%  
    - **Precision:** 62.8%  
    - **F1 Score:** 73.0%  
    - **Threshold:** 0.2 (favor recall over precision)  
    """)

#######################
# Model Overview Section

st.markdown("### About This App")
st.markdown("""
This app predicts whether a network session is likely to be a cyberattack based on session-level characteristics 
like packet size, login attempts, encryption type, and IP reputation score.

The underlying model was trained on a labeled intrusion detection dataset using LightGBM, a fast and accurate gradient boosting framework.
This project demonstrates real-time predictions via a deployed API, and provides insight into the features most correlated with attack behavior.
""")

#######################
# Intrusion Prediction Using API
st.markdown("### 🔍 Intrusion Detection Prediction")

# Input fields for real-time attack detection
protocol_type = st.selectbox("Protocol Type", ["TCP", "UDP", "ICMP"])
encryption_used = st.selectbox("Encryption Used", ["AES", "DES", "None"])
packet_size = st.number_input("Network Packet Size", value=500)
login_attempts = st.number_input("Login Attempts", value=3)
session_duration = st.number_input("Session Duration", value=500.0)
ip_reputation = st.number_input("IP Reputation Score", value=0.5)
failed_logins = st.number_input("Failed Logins", value=1)
unusual_access = st.checkbox("Unusual Time Access")

# Manually apply one-hot encoding
protocol_tcp = 1 if protocol_type == "TCP" else 0
protocol_udp = 1 if protocol_type == "UDP" else 0
encryption_des = 1 if encryption_used == "DES" else 0
encryption_none = 1 if encryption_used == "None" else 0

# API URL
API_URL = "https://e-eeeema-intrusion-detection.hf.space/predict"

if st.button("Predict Attack"):
    features = [
        packet_size,
        login_attempts,
        session_duration,
        ip_reputation,
        failed_logins,
        int(unusual_access),
        protocol_tcp,
        protocol_udp,
        encryption_des,
        encryption_none
    ]

    response = requests.post(API_URL, json={"features": features})

    if response.status_code == 200:
        result = response.json()
        prediction = response.json().get("attack_detected", 0)
        probability = result.get("probability", 0.0)

        st.markdown(f"**🧮 Prediction Confidence:** `{probability*100:.2f}%`")

        if prediction == 1:
            st.error("🚨 Attack Detected!")
            st.markdown("""
            > **Why?** The model flagged this session as an intrusion based on a combination of:
            - Suspicious IP reputation
            - Multiple failed login attempts
            - Unusual access time or weak encryption
            """)
        else:
            st.success("✅ No Attack Detected.")
            st.markdown("> **Why?** The session appears typical and shows no strong indicators of intrusion.")

        # Confidence interpretation
        if probability >= 0.7:
            st.info("🔍 High model confidence in this prediction.")
        elif probability >= 0.4:
            st.warning("⚠️ Medium confidence – results should be interpreted with caution.")
        else:
            st.warning("❗ Low confidence – the model is uncertain about this prediction.")
    else:
        st.error("⚠️ API request failed. Please check the API URL.")


#######################
# Resources

st.markdown("#### 🔗 Resources")
st.markdown("""
- 📂 [View Model Training Code on GitHub](https://github.com/butlerem/intrusion-detection-model-lgbm/blob/main/intrusion_detector.ipynb)  
- 📊 [View Kaggle Dataset](https://www.kaggle.com/code/nukimayasari/cybersecurity-intrusion)
""")
