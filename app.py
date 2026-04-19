import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Disease Prediction")

st.title("❤️ Heart Disease Prediction")

# User input
def user_input():
    age = st.slider("Age", 20, 80, 45)
    sex = st.selectbox("Sex (1=Male, 0=Female)", [1, 0])
    cp = st.slider("Chest Pain Type", 0, 3, 1)
    trestbps = st.slider("Blood Pressure", 80, 200, 120)
    chol = st.slider("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Sugar >120", [1, 0])
    restecg = st.slider("Rest ECG", 0, 2, 1)
    thalach = st.slider("Max Heart Rate", 70, 210, 150)
    exang = st.selectbox("Exercise Angina", [1, 0])
    oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)
    slope = st.slider("Slope", 0, 2, 1)
    ca = st.slider("Vessels", 0, 4, 0)
    thal = st.slider("Thal", 1, 3, 2)

    data = [age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal]

    return np.array(data).reshape(1, -1)

input_data = user_input()

if st.button("Predict"):
    scaled = scaler.transform(input_data)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    if pred == 1:
        st.error(f"⚠️ High Risk ({prob:.2f})")
    else:
        st.success(f"✅ Low Risk ({prob:.2f})")
