import streamlit as st

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.write("""
This project was developed as a capstone project during the **A2IT InternEdge Internship**.

The objective is to build an AI-powered system that predicts:

- 💰 Insurance Premium Amount
- ⚠️ Insurance Claim Risk

while providing transparency through simple explainability.
""")

st.divider()

# --------------------------------------------------

st.header("📌 Problem Statement")

st.info("""
Insurance companies calculate premium amounts using many customer-related factors.
Customers often do not understand why their premium is high or low.

This project predicts:

• Insurance Premium

• Insurance Claim Risk

using Machine Learning models while providing simple explanations for the prediction.
""")

st.divider()

# --------------------------------------------------

st.header("🎯 Project Objectives")

st.markdown("""

- Generate a synthetic insurance dataset

- Perform Exploratory Data Analysis (EDA)

- Perform Statistical Analysis

- Predict Insurance Premium

- Predict Insurance Claim Probability

- Compare Multiple Machine Learning Models

- Build Artificial Neural Network (ANN)

- Deploy using Streamlit

""")

st.divider()

# --------------------------------------------------

st.header("📂 Dataset Features")

features = [
    "Age",
    "BMI",
    "Smoking",
    "Previous Claims",
    "Policy Type",
    "Annual Income",
    "Exercise Level",
    "Premium Amount",
    "Claim"
]

st.table(features)

st.divider()

# --------------------------------------------------

st.header("🤖 Machine Learning Models")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Regression")

    st.markdown("""

- Linear Regression

- Decision Tree Regressor

- Random Forest Regressor

- XGBoost Regressor

""")

with col2:

    st.subheader("Classification")

    st.markdown("""

- Logistic Regression

- Decision Tree Classifier

- Random Forest Classifier

- XGBoost Classifier

""")

st.divider()

# --------------------------------------------------

st.header("🧠 Artificial Neural Network")

st.write("""

A simple ANN model was developed for:

• Premium Prediction

• Claim Prediction

The ANN performance was compared with traditional machine learning algorithms.

""")

st.divider()

# --------------------------------------------------

st.header("🛠 Technologies Used")

st.markdown("""

- Python

- Streamlit

- Pandas

- NumPy

- Scikit-Learn

- TensorFlow

- XGBoost

- Plotly

- Joblib

""")

st.divider()

# --------------------------------------------------

st.header("📈 Project Workflow")

st.markdown("""

1. Dataset Generation

2. Data Cleaning

3. Exploratory Data Analysis

4. Statistical Analysis

5. Regression Models

6. Classification Models

7. ANN

8. Model Comparison

9. Streamlit Deployment

""")

st.divider()

# --------------------------------------------------

st.header("👨‍💻 Developer")

st.success("""

**Project Title**

Insurance Claim Risk & Premium Predictor with Explainability

Developed by:

**Tejnoor Singh**

BCA (Hons.) AI & ML

Akal University

Capstone Project – A2IT InternEdge Internship

""")

st.divider()

st.caption("© 2026 Insurance Claim Risk & Premium Predictor")
