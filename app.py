import streamlit as st
import joblib
import numpy as np

# Load your trained model and scaler
model = joblib.load('fraud_xgb_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("💳 Credit Card Fraud Detection")
st.write("Enter input features below:")

# Inputs: V1 to V28 and Amount
features = [f'V{i}' for i in range(1, 29)] + ['Amount']
user_input = []

for f in features:
    val = st.number_input(f, value=0.0)
    user_input.append(val)

if st.button("Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraudulent transaction detected! (Risk: {probability:.2%})")
    else:
        st.success(f"✅ Legitimate transaction. (Risk: {probability:.2%})")
