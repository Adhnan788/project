
import streamlit as st
import joblib
import numpy as np

st.title("Credit Fraud Detection")

model = joblib.load("C:\\Users\\apadh\\OneDrive\\Desktop\\project\\credit_card\\rf.pkl")
scaler = joblib.load("C:\\Users\\apadh\\OneDrive\\Desktop\\project\\credit_card\\scaler.pkl")

amount = st.number_input("Transaction Amount")
transaction_hour = st.slider("Transaction Hour", 0, 23)
foreign_transaction = st.selectbox("Foreign Transaction", ["No", "Yes"])
location_mismatch = st.selectbox("Location Mismatch", ["No", "Yes"])
device_trust_score = st.slider("Device Trust Score", 0.0, 1.0)
velocity_last_24h = st.number_input("Transactions in last 24h")
foreign_transaction = {'No': 0, 'Yes': 1}[foreign_transaction]
location_mismatch = {'No': 0, 'Yes': 1}[location_mismatch]

if st.button("Predict Fraud"):

    data = np.array([[amount,
                      transaction_hour,
                      foreign_transaction,
                      location_mismatch,
                      device_trust_score,
                      velocity_last_24h]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Fraud Transaction ⚠️")
    else:
        st.success("Legitimate Transaction ✅")