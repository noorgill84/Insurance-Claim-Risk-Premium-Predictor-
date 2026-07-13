import streamlit as st

# ------------------ Page Configuration ------------------ #
st.set_page_config(
    page_title="Insurance Claim Risk & Premium Predictor",
    page_icon="🛡️",
    layout="wide"
)

# ------------------ Header ------------------ #
st.title("🛡️ Insurance Claim Risk & Premium Predictor")
st.markdown(
    """
Welcome to the **Insurance Claim Risk & Premium Predictor**.

This application predicts:

- 💰 Insurance Premium Amount
- ⚠️ Insurance Claim Probability
- 📊 Model Performance
- 🤖 Explainable AI Results
"""
)

st.divider()

# ------------------ Features ------------------ #
col1, col2 = st.columns(2)

with col1:
    st.info("💰 **Premium Prediction**\n\nPredict the insurance premium using customer details.")

with col2:
    st.warning("⚠️ **Claim Prediction**\n\nPredict whether a customer is likely to make an insurance claim.")

st.divider()

# ------------------ Workflow ------------------ #
st.subheader("🔄 Project Workflow")

st.markdown("""
1. Load Insurance Dataset
2. Perform Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Statistical Analysis
5. Premium Prediction (Regression)
6. Claim Prediction (Classification)
7. Artificial Neural Network (ANN)
8. Explainability
9. Deploy using Streamlit
""")

st.divider()

# ------------------ Sidebar ------------------ #
st.sidebar.success("Select a page from the sidebar.")
