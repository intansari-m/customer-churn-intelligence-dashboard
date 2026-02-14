import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import numpy as np

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="CLTV & Retention Strategy",
    page_icon="📈",
    layout="wide"
)

st.title("📈 CLTV Strategy & Retention Targeting")
st.markdown("### High-Value Customer Protection & Risk Segmentation")

st.markdown("""
This section identifies high-value customers at churn risk
and segments them into strategic retention priority tiers.
Designed for revenue protection and customer lifecycle optimization.
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
# CREATE RISK SEGMENTATION
# ======================================================

# CLTV Tier
df["cltv_tier"] = pd.qcut(
    df["cltv"],
    q=3,
    labels=["Low Value", "Mid Value", "High Value"]
)

# Churn Risk Tier
df["risk_tier"] = pd.qcut(
    df["churn_score"],
    q=3,
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

# Priority Segment
df["retention_priority"] = np.where(
    (df["cltv_tier"] == "High Value") & (df["risk_tier"] == "High Risk"),
    "Critical Retention",
    np.where(
        (df["cltv_tier"] == "High Value"),
        "High Value - Monitor",
        "Standard"
    )
)

# ======================================================
# SIDEBAR FILTERS
# ======================================================
st.sidebar.header("🔎 Retention Filters")

priority_filter = st.sidebar.multiselect(
    "Retention Priority",
    options=df["retention_priority"].unique(),
    default=df["retention_priority"].unique()
)

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["contract"].unique(),
    default=df["contract"].unique()
)

filtered_df = df[
    (df["retention_priority"].isin(priority_filter)) &
    (df["contract"].isin(contract_filter))
]

# ======================================================
# KPI SECTION
# ======================================================
st.subheader("📌 Retention Priority Metrics")

total_customers = filtered_df["customer_id"].nunique()
critical_customers = filtered_df[filtered_df["retention_priority"] == "Critical Retention"].shape[0]
total_revenue = filtered_df["total_revenue"].sum()
avg_cltv = filtered_df["cltv"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Critical Retention Accounts", f"{critical_customers:,}")
col3.metric("Revenue at Scope", f"${total_revenue:,.0f}")
col4.metric("Average CLTV", f"${avg_cltv:,.0f}")

st.divider()

# ======================================================
# CLTV vs CHURN SCORE MATRIX
# ======================================================
st.subheader("CLTV vs Churn Risk Matrix")

fig_matrix = px.scatter(
    filtered_df,
    x="churn_score",
    y="cltv",
    color="retention_priority",
    size="monthly_charges",
    hover_data=[
        "customer_id",
        "contract",
        "tenure_in_months",
        "churn_label"
    ]
)

st.plotly_chart(fig_matrix, use_container_width=True)

st.divider()

# ======================================================
# PRIORITY DISTRIBUTION
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Retention Priority Distribution")

    priority_dist = (
        filtered_df.groupby("retention_priority")
        .size()
        .reset_index(name="count")
    )

    fig_priority = px.pie(
        priority_dist,
        names="retention_priority",
        values="count",
        hole=0.5
    )

    st.plotly_chart(fig_priority, use_container_width=True)

with col2:
    st.subheader("Revenue by Retention Segment")

    revenue_priority = (
        filtered_df.groupby("retention_priority")["total_revenue"]
        .sum()
        .reset_index()
    )

    fig_revenue = px.bar(
        revenue_priority,
        x="retention_priority",
        y="total_revenue"
    )

    st.plotly_chart(fig_revenue, use_container_width=True)

st.divider()

# ======================================================
# CONTRACT IMPACT ON PRIORITY
# ======================================================
st.subheader("Contract Distribution by Retention Priority")

contract_priority = (
    filtered_df.groupby(["contract", "retention_priority"])
    .size()
    .reset_index(name="count")
)

fig_contract = px.bar(
    contract_priority,
    x="contract",
    y="count",
    color="retention_priority",
    barmode="group"
)

st.plotly_chart(fig_contract, use_container_width=True)

st.divider()

# ======================================================
# STRATEGIC RECOMMENDATION
# ======================================================
st.subheader("📌 Strategic Retention Recommendations")

st.markdown("""
**1. Critical Retention Segment**
- High CLTV + High Risk customers must receive proactive retention outreach.
- Offer loyalty incentives or contract migration programs.

**2. High Value - Monitor**
- Maintain engagement programs.
- Prevent migration to higher churn risk tier.

**3. Standard Segment**
- Focus on automation and scalable engagement strategies.

**4. Contract Optimization**
- Transition high-risk month-to-month customers to longer contracts.

**5. Revenue Protection Strategy**
- Prioritize retention investment toward high-value high-risk clusters.
""")

st.caption("Customer Churn Intelligence Dashboard – CLTV & Strategic Retention Modeling")
