import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------- Page Configuration ---------------------- #
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------- Title ---------------------- #
st.title("📊 Insurance Dashboard")
st.write("Overview of the Insurance Dataset")

# ---------------------- Load Dataset ---------------------- #
@st.cache_data
def load_data():
    return pd.read_csv("data/insurance_data_cleaned.csv")

df = load_data()

# ---------------------- Dataset Preview ---------------------- #
with st.expander("👀 View Dataset"):
    st.dataframe(df.head())

# ---------------------- KPI Cards ---------------------- #
total_customers = len(df)
average_age = round(df["Age"].mean(), 1)
average_premium = round(df["Premium_Amount"].mean(), 2)
claim_rate = round(df["Claim"].mean() * 100, 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total Customers", total_customers)
col2.metric("🎂 Average Age", average_age)
col3.metric("💰 Average Premium", f"₹ {average_premium}")
col4.metric("⚠️ Claim Rate", f"{claim_rate}%")

st.divider()

# ---------------------- Premium Distribution ---------------------- #
st.subheader("💰 Premium Distribution")

fig = px.histogram(
    df,
    x="Premium_Amount",
    nbins=20,
    title="Distribution of Premium Amount"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------- Age Distribution ---------------------- #
st.subheader("🎂 Age Distribution")

fig = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------- Policy Type ---------------------- #
st.subheader("📑 Policy Type Distribution")

policy_count = df["Policy_Type"].value_counts().reset_index()
policy_count.columns = ["Policy Type", "Count"]

fig = px.pie(
    policy_count,
    names="Policy Type",
    values="Count",
    hole=0.4,
    title="Policy Types"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------- Smoking Distribution ---------------------- #
st.subheader("🚬 Smoking Distribution")

smoking_count = df["Smoking"].value_counts().reset_index()
smoking_count.columns = ["Smoking", "Count"]

fig = px.bar(
    smoking_count,
    x="Smoking",
    y="Count",
    color="Smoking",
    title="Smoking Status"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------- Claim Distribution ---------------------- #
st.subheader("⚠️ Claim Distribution")

claim_count = df["Claim"].value_counts().reset_index()
claim_count.columns = ["Claim", "Count"]

claim_count["Claim"] = claim_count["Claim"].replace({
    0: "No Claim",
    1: "Claim"
})

fig = px.pie(
    claim_count,
    names="Claim",
    values="Count",
    title="Claim Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------- Premium by Policy ---------------------- #
st.subheader("📈 Average Premium by Policy Type")

premium_policy = (
    df.groupby("Policy_Type")["Premium_Amount"]
    .mean()
    .reset_index()
)

fig = px.bar(
    premium_policy,
    x="Policy_Type",
    y="Premium_Amount",
    color="Policy_Type",
    title="Average Premium by Policy Type"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------- Summary ---------------------- #
st.divider()

st.success("✅ Dashboard loaded successfully!")

st.markdown("""
### Dashboard Summary

- Total number of customers
- Average customer age
- Average premium amount
- Insurance claim percentage
- Premium distribution
- Policy type distribution
- Smoking status distribution
- Claim distribution
""")
