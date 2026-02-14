import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="Executive Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Intelligence Dashboard")
st.markdown("### Executive-Level Business Overview for Strategic Decision Making")

st.markdown("""
This page provides a high-level summary of customer performance,
churn exposure, and revenue concentration.
Designed for stakeholders and decision-makers.
""")

# ======================================================
# LOAD DATA
# ======================================================
@st.cache_data
def load_data():
    base_path = Path(__file__).resolve().parent.parent
    data_path = base_path / "data" / "final_dataset.csv"
    df = pd.read_csv(data_path)
    df.columns = df.columns.str.lower().str.strip()
    return df

df = load_data()

# ======================================================
# SIDEBAR FILTERS
# ======================================================
st.sidebar.header("🔎 Executive Filters")

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["contract"].unique(),
    default=df["contract"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Internet Service",
    options=df["internet_service"].unique(),
    default=df["internet_service"].unique()
)

state_filter = st.sidebar.multiselect(
    "State",
    options=df["state"].unique(),
    default=df["state"].unique()
)

tenure_range = st.sidebar.slider(
    "Tenure (Months)",
    int(df["tenure_in_months"].min()),
    int(df["tenure_in_months"].max()),
    (
        int(df["tenure_in_months"].min()),
        int(df["tenure_in_months"].max())
    )
)

# ======================================================
# APPLY FILTERS
# ======================================================
filtered_df = df[
    (df["contract"].isin(contract_filter)) &
    (df["internet_service"].isin(internet_filter)) &
    (df["state"].isin(state_filter)) &
    (df["tenure_in_months"].between(tenure_range[0], tenure_range[1]))
]

# ======================================================
# KPI SECTION
# ======================================================
st.subheader("📌 Key Performance Indicators")

total_customers = filtered_df["customer_id"].nunique()
total_churn = filtered_df[filtered_df["churn_label"] == "Yes"].shape[0]
churn_rate = (total_churn / total_customers) * 100 if total_customers > 0 else 0
total_revenue = filtered_df["total_revenue"].sum()
avg_cltv = filtered_df["cltv"].mean() if total_customers > 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{total_churn:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Total Revenue", f"${total_revenue:,.0f}")
col5.metric("Average CLTV", f"${avg_cltv:,.0f}")

st.divider()

# ======================================================
# CHURN DISTRIBUTION
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Status Distribution")

    fig_status = px.pie(
        filtered_df,
        names="customer_status",
        hole=0.5
    )

    st.plotly_chart(fig_status, use_container_width=True)

with col2:
    st.subheader("Churn by Contract Type")

    contract_churn = (
        filtered_df.groupby(["contract", "churn_label"])
        .size()
        .reset_index(name="count")
    )

    fig_contract = px.bar(
        contract_churn,
        x="contract",
        y="count",
        color="churn_label",
        barmode="group"
    )

    st.plotly_chart(fig_contract, use_container_width=True)

st.divider()

# ======================================================
# REVENUE & TENURE INSIGHT
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Contract")

    revenue_contract = (
        filtered_df.groupby("contract")["total_revenue"]
        .sum()
        .reset_index()
        .sort_values(by="total_revenue", ascending=False)
    )

    fig_revenue = px.bar(
        revenue_contract,
        x="contract",
        y="total_revenue"
    )

    st.plotly_chart(fig_revenue, use_container_width=True)

with col2:
    st.subheader("Tenure vs Churn Behavior")

    fig_tenure = px.box(
        filtered_df,
        x="churn_label",
        y="tenure_in_months"
    )

    st.plotly_chart(fig_tenure, use_container_width=True)

st.divider()

# ======================================================
# STRATEGIC INSIGHT SECTION
# ======================================================
st.subheader("📌 Executive Insights")

st.markdown("""
- Month-to-month contracts consistently exhibit higher churn exposure.
- Customers with shorter tenure are significantly more likely to churn.
- Revenue concentration is heavily influenced by contract structure.
- Long-term contracts contribute to higher average CLTV.
- Filtering allows leadership to simulate risk segmentation dynamically.
""")

st.caption("Data Analyst Portfolio Project – Customer Churn Intelligence")
