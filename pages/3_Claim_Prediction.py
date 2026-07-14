import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="Claim Prediction",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Insurance Claim Prediction")
st.write("Enter the customer details to predict the insurance claim risk.")

# ---------------- Load Model ---------------- #

MODEL_PATH = "models/claim_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ claim_model.pkl not found inside models folder.")
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

# ---------------- Prediction ---------------- #

if st.button("🚀 Predict Claim", use_container_width=True):

    input_data = pd.DataFrame({
         "Customer_ID":[1],

        "Age":[age],

        "BMI":[bmi],

        "Smoking":[smoking],

        "Previous_Claims":[previous_claims],

        "Policy_Type":[policy],

        "Annual_Income":[annual_income],

        "Exercise_Level":[exercise]

    })

    prediction = model.predict(input_data)[0]

    probability = None

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0][1] * 100

    st.divider()

    # ---------------- Result ---------------- #

    if prediction == 1:

        st.error("⚠️ Claim Likely")

    else:

        st.success("✅ Claim Not Likely")

    if probability is not None:

        st.metric(
            "Claim Probability",
            f"{probability:.2f}%"
        )

        if probability < 30:

            st.success("🟢 Risk Level : LOW")

        elif probability < 70:

            st.warning("🟠 Risk Level : MEDIUM")

        else:

            st.error("🔴 Risk Level : HIGH")

    st.divider()

    # ---------------- Explanation ---------------- #

    st.subheader("Why this Prediction?")

    explanation = []

    if smoking == 1:
        explanation.append("🚬 Smoking increases the likelihood of insurance claims.")

    if previous_claims >= 2:
        explanation.append("📄 Multiple previous claims increase future claim risk.")

    if age >= 55:
        explanation.append("👴 Higher age contributes to increased claim probability.")

    if bmi >= 30:
        explanation.append("⚖️ High BMI may increase health-related insurance risk.")

    if exercise == 2:
        explanation.append("🏃 Regular exercise reduces health risk.")

    if len(explanation) == 0:
        explanation.append("✅ No significant risk factors detected.")

    for item in explanation:
        st.info(item)

    st.divider()

    # ---------------- Customer Summary ---------------- #

    st.subheader("Prediction Summary")

    summary = pd.DataFrame({
         "Customer_ID":[1],

        "Age":[age],

        "BMI":[bmi],

        "Smoking":["Yes" if smoking else "No"],

        "Previous Claims":[previous_claims],

        "Policy":["Basic","Standard","Premium"][policy],

        "Annual Income":[annual_income],

        "Exercise":["Low","Medium","High"][exercise],

        "Prediction":["Claim Likely" if prediction else "No Claim"]

    })

    st.dataframe(summary, use_container_width=True)
