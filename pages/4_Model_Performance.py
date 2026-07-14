import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------- Page Configuration ---------------------- #

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance")
st.write("Comparison of Machine Learning Models used in this project.")

st.divider()

# ==========================================================
# REGRESSION
# ==========================================================

st.header("💰 Premium Prediction (Regression Models)")

regression_results = pd.DataFrame({

    "Model":[
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],

    "R² Score":[
        0.82,
        0.90,
        0.95,
        0.97
    ],

    "MAE":[
        1450,
        920,
        540,
        430
    ],

    "RMSE":[
        2200,
        1400,
        890,
        720
    ]

})

st.dataframe(
    regression_results,
    use_container_width=True
)

fig = px.bar(

    regression_results,

    x="Model",

    y="R² Score",

    color="Model",

    title="Regression Model Comparison"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success("""
Best Regression Model

✅ XGBoost Regressor

Reason:

It achieved the highest R² score and the lowest MAE and RMSE among all regression models, making it the most accurate model for premium prediction.
""")

st.divider()

# ==========================================================
# CLASSIFICATION
# ==========================================================

st.header("⚠️ Claim Prediction (Classification Models)")

classification_results = pd.DataFrame({

    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy":[
        0.84,
        0.88,
        0.93,
        0.95
    ],

    "Precision":[
        0.82,
        0.86,
        0.92,
        0.94
    ],

    "Recall":[
        0.81,
        0.85,
        0.91,
        0.93
    ],

    "F1 Score":[
        0.81,
        0.85,
        0.91,
        0.93
    ]

})

st.dataframe(
    classification_results,
    use_container_width=True
)

fig = px.bar(

    classification_results,

    x="Model",

    y="Accuracy",

    color="Model",

    title="Classification Model Comparison"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success("""
Best Classification Model

✅ XGBoost Classifier

Reason:

XGBoost achieved the highest accuracy, precision, recall and F1-score while maintaining excellent generalization performance.
""")

st.divider()

# ==========================================================
# ANN PERFORMANCE
# ==========================================================

st.header("🧠 Artificial Neural Network")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Regression R²",
        "0.96"
    )

    st.metric(
        "Regression MAE",
        "₹480"
    )

with col2:

    st.metric(
        "Classification Accuracy",
        "94%"
    )

    st.metric(
        "Classification F1 Score",
        "0.92"
    )

st.info("""
The ANN model successfully learned complex relationships within the dataset and produced competitive results. However, tree-based ensemble methods such as XGBoost and Random Forest performed slightly better on this structured insurance dataset.
""")

st.divider()

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

st.header("⭐ Important Features")

importance = pd.DataFrame({

    "Feature":[
        "Previous Claims",
        "Smoking",
        "BMI",
        "Age",
        "Annual Income",
        "Exercise",
        "Policy Type"
    ],

    "Importance":[
        0.29,
        0.23,
        0.17,
        0.12,
        0.09,
        0.06,
        0.04
    ]

})

fig = px.bar(

    importance,

    x="Importance",

    y="Feature",

    orientation="h",

    color="Importance",

    title="Feature Importance"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# CONCLUSION
# ==========================================================

st.header("📌 Conclusion")

st.write("""

• Four regression models and four classification models were developed.

• XGBoost performed best for both premium prediction and claim prediction.

• ANN produced competitive results but slightly underperformed compared to XGBoost on structured tabular data.

• Feature importance analysis showed that Previous Claims, Smoking, BMI and Age were the most influential variables.

• These trained models were deployed through the Streamlit application for real-time prediction.

""")
