import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="Churn Risk Deep Dive",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Churn Risk Deep Dive")
st.markdown("### Behavioral & Service-Level Churn Risk Analysis")

st.markdown("""
This section identifies key churn drivers based on customer behavior,
service adoption, satisfaction levels, and churn classification.
Designed to uncover actionable retention insights.
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
st.sidebar.header("🔎 Churn Risk Filters")

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

churn_filter = st.sidebar.multiselect(
    "Churn Label",
    options=df["churn_label"].unique(),
    default=df["churn_label"].unique()
)

filtered_df = df[
    (df["contract"].isin(contract_filter)) &
    (df["internet_service"].isin(internet_filter)) &
    (df["churn_label"].isin(churn_filter))
]

# ======================================================
# KPI SECTION
# ======================================================
st.subheader("📌 Churn Risk Indicators")

total_customers = filtered_df["customer_id"].nunique()
churned_customers = filtered_df[filtered_df["churn_label"] == "Yes"].shape[0]
churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0
avg_satisfaction = filtered_df["satisfaction_score"].mean()
avg_churn_score = filtered_df["churn_score"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Avg Satisfaction", f"{avg_satisfaction:.2f}")
col5.metric("Avg Churn Score", f"{avg_churn_score:.1f}")

st.divider()

# ======================================================
# CHURN BY CONTRACT
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Rate by Contract")

    churn_contract = (
        filtered_df.groupby("contract")["churn_value"]
        .mean()
        .reset_index()
    )

    churn_contract["churn_rate"] = churn_contract["churn_value"] * 100

    fig_contract = px.bar(
        churn_contract,
        x="contract",
        y="churn_rate"
    )

    st.plotly_chart(fig_contract, use_container_width=True)

with col2:
    st.subheader("Satisfaction vs Churn")

    fig_satisfaction = px.box(
        filtered_df,
        x="churn_label",
        y="satisfaction_score",
        color="churn_label"
    )

    st.plotly_chart(fig_satisfaction, use_container_width=True)

st.divider()

# ======================================================
# SERVICE IMPACT ANALYSIS
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Online Security vs Churn")

    security_churn = (
        filtered_df.groupby(["online_security", "churn_label"])
        .size()
        .reset_index(name="count")
    )

    fig_security = px.bar(
        security_churn,
        x="online_security",
        y="count",
        color="churn_label",
        barmode="group"
    )

    st.plotly_chart(fig_security, use_container_width=True)

with col2:
    st.subheader("Tech Support vs Churn")

    support_churn = (
        filtered_df.groupby(["premium_tech_support", "churn_label"])
        .size()
        .reset_index(name="count")
    )

    fig_support = px.bar(
        support_churn,
        x="premium_tech_support",
        y="count",
        color="churn_label",
        barmode="group"
    )

    st.plotly_chart(fig_support, use_container_width=True)

st.divider()

# ======================================================
# CHURN CATEGORY & REASON
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Category Distribution")

    churn_category = (
        filtered_df[filtered_df["churn_label"] == "Yes"]
        .groupby("churn_category")
        .size()
        .reset_index(name="count")
        .sort_values(by="count", ascending=False)
    )

    fig_category = px.bar(
        churn_category,
        x="churn_category",
        y="count"
    )

    st.plotly_chart(fig_category, use_container_width=True)

with col2:
    st.subheader("Churn Score Distribution")

    fig_score = px.histogram(
        filtered_df,
        x="churn_score",
        nbins=30,
        color="churn_label"
    )

    st.plotly_chart(fig_score, use_container_width=True)

st.divider()

# ======================================================
# STRATEGIC INSIGHT
# ======================================================
st.subheader("📌 Churn Risk Insights")

st.markdown("""
- Month-to-month contracts exhibit significantly higher churn rates.
- Lower satisfaction scores strongly correlate with churn behavior.
- Customers without online security or tech support show elevated churn risk.
- High churn score segments align with short tenure and limited service adoption.
- Targeted retention programs should prioritize early-tenure customers.
""")

st.caption("Customer Churn Intelligence Dashboard – Behavioral Risk Analysis")
