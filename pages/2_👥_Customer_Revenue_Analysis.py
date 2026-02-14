import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="Customer & Revenue Analysis",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Customer & Revenue Analysis")
st.markdown("### Revenue Drivers, Customer Segmentation & Profitability Insights")

st.markdown("""
This page analyzes revenue contribution, pricing behavior,
payment structure, and customer lifetime value segmentation.
Designed for business and growth strategy evaluation.
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
st.sidebar.header("🔎 Revenue Filters")

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["contract"].unique(),
    default=df["contract"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options=df["payment_method"].unique(),
    default=df["payment_method"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Internet Service",
    options=df["internet_service"].unique(),
    default=df["internet_service"].unique()
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
    (df["payment_method"].isin(payment_filter)) &
    (df["internet_service"].isin(internet_filter)) &
    (df["tenure_in_months"].between(tenure_range[0], tenure_range[1]))
]

# ======================================================
# KPI SECTION
# ======================================================
st.subheader("📌 Revenue Performance Indicators")

total_revenue = filtered_df["total_revenue"].sum()
avg_monthly_charge = filtered_df["monthly_charges"].mean()
avg_cltv = filtered_df["cltv"].mean()
avg_tenure = filtered_df["tenure_in_months"].mean()
total_customers = filtered_df["customer_id"].nunique()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Avg Monthly Charges", f"${avg_monthly_charge:,.2f}")
col3.metric("Average CLTV", f"${avg_cltv:,.0f}")
col4.metric("Average Tenure", f"{avg_tenure:.1f} months")
col5.metric("Total Customers", f"{total_customers:,}")

st.divider()

# ======================================================
# MONTHLY CHARGE & CLTV DISTRIBUTION
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Monthly Charges by Contract")

    fig_monthly = px.box(
        filtered_df,
        x="contract",
        y="monthly_charges",
        color="contract"
    )

    st.plotly_chart(fig_monthly, use_container_width=True)

with col2:
    st.subheader("CLTV Distribution by Contract")

    fig_cltv = px.box(
        filtered_df,
        x="contract",
        y="cltv",
        color="contract"
    )

    st.plotly_chart(fig_cltv, use_container_width=True)

st.divider()

# ======================================================
# PAYMENT & INTERNET IMPACT
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Payment Method")

    revenue_payment = (
        filtered_df.groupby("payment_method")["total_revenue"]
        .sum()
        .reset_index()
        .sort_values(by="total_revenue", ascending=False)
    )

    fig_payment = px.bar(
        revenue_payment,
        x="payment_method",
        y="total_revenue"
    )

    st.plotly_chart(fig_payment, use_container_width=True)

with col2:
    st.subheader("Monthly Charges by Internet Service")

    fig_internet = px.box(
        filtered_df,
        x="internet_service",
        y="monthly_charges",
        color="internet_service"
    )

    st.plotly_chart(fig_internet, use_container_width=True)

st.divider()

# ======================================================
# TENURE vs CLTV ANALYSIS (ADVANCED SCATTER)
# ======================================================
st.subheader("Tenure vs CLTV Relationship")

fig_scatter = px.scatter(
    filtered_df,
    x="tenure_in_months",
    y="cltv",
    color="contract",
    size="monthly_charges",
    hover_data=[
        "customer_id",
        "payment_method",
        "internet_service",
        "churn_label"
    ]
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# ======================================================
# STRATEGIC BUSINESS INSIGHT
# ======================================================
st.subheader("📌 Revenue & Segmentation Insights")

st.markdown("""
- Long-term contracts generate significantly higher CLTV and revenue stability.
- Month-to-month customers exhibit volatile revenue behavior.
- Electronic check payment users require closer churn monitoring.
- Higher monthly charges correlate with larger CLTV potential.
- Tenure duration remains the strongest predictor of long-term profitability.
""")

st.caption("Customer Churn Intelligence Dashboard – Revenue Deep Dive")
