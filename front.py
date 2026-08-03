import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
model = pickle.load(open('crop_model.pkl', 'rb'))

st.set_page_config(page_title="Crop Predictor", page_icon="crop")

st.title("Smart Crop Recommendation System")
st.markdown("Enter your soil and weather details to find the best crop to grow.")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    n = st.number_input("Nitrogen (N)", 0, 140, 50)
    p = st.number_input("Phosphorus (P)", 0, 145, 50)
    k = st.number_input("Potassium (K)", 0, 205, 50)
    temp = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)

with col2:
    hum = st.slider("Humidity (%)", 0.0, 100.0, 70.0)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)
    rain = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

# Prediction Logic
if st.button("Recommend Best Crop"):
    features = np.array([[n, p, k, temp, hum, ph, rain]])
    prediction = model.predict(features)
    
    st.balloons()
    st.success(f"### The best crop for your field is: **{prediction[0].upper()}**")