import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="Premium Prediction",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Insurance Premium Prediction")
st.write("Enter the customer details below to predict the insurance premium.")

# ---------------- Load Model ---------------- #

MODEL_PATH = "models/premium_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ premium_model.pkl not found inside models folder.")
    st.stop()

model = joblib.load(MODEL_PATH)

# ---------------- Input Form ---------------- #

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        18,
        80,
        30
    )

    bmi = st.slider(
        "BMI",
        15.0,
        40.0,
        24.0
    )

    smoking = st.selectbox(
        "Smoking",
        ["No", "Yes"]
    )

    previous_claims = st.number_input(
        "Previous Claims",
        min_value=0,
        max_value=10,
        value=0
    )

with col2:

    policy = st.selectbox(
        "Policy Type",
        ["Basic", "Standard", "Premium"]
    )

    annual_income = st.number_input(
        "Annual Income (₹)",
        min_value=100000,
        max_value=5000000,
        value=500000,
        step=10000
    )

    exercise = st.selectbox(
        "Exercise Level",
        ["Low", "Medium", "High"]
    )

# ---------------- Encoding ---------------- #

smoking = 1 if smoking == "Yes" else 0

policy_mapping = {
    "Basic": 0,
    "Standard": 1,
    "Premium": 2
}

exercise_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

policy = policy_mapping[policy]
exercise = exercise_mapping[exercise]

# ---------------- Prediction Button ---------------- #

if st.button("🚀 Predict Premium", use_container_width=True):

    input_data = pd.DataFrame({

        "Age":[age],

        "BMI":[bmi],

        "Smoking":[smoking],

        "Previous_Claims":[previous_claims],

        "Policy_Type":[policy],

        "Annual_Income":[annual_income],

        "Exercise_Level":[exercise]

    })

    prediction = model.predict(input_data)

    premium = round(float(prediction[0]),2)

    st.success(f"### 💰 Predicted Premium: ₹ {premium}")

    st.divider()

    st.subheader("Why this Premium?")

    explanation = []

    if smoking == 1:
        explanation.append("🚬 Smoking generally increases insurance premium.")

    if previous_claims > 0:
        explanation.append("📄 Previous claims increase insurance risk.")

    if age > 50:
        explanation.append("👴 Higher age may increase premium.")

    if exercise == 2:
        explanation.append("🏃 Healthy lifestyle may reduce premium.")

    if annual_income > 1000000:
        explanation.append("💼 Higher income influences premium calculation.")

    if len(explanation) == 0:
        explanation.append("✅ No major risk factors detected.")

    for item in explanation:
        st.info(item)

    st.divider()

    st.subheader("Customer Summary")

    summary = pd.DataFrame({

        "Age":[age],

        "BMI":[bmi],

        "Smoking":["Yes" if smoking==1 else "No"],

        "Previous Claims":[previous_claims],

        "Policy":["Basic","Standard","Premium"][policy],

        "Annual Income":[annual_income],

        "Exercise":["Low","Medium","High"][exercise],

        "Predicted Premium":[premium]

    })

    st.dataframe(summary,use_container_width=True)
