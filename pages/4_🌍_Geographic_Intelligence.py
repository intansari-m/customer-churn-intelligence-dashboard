import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="Geographic Intelligence",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Geographic & Regional Intelligence")
st.markdown("### Regional Revenue Distribution & Churn Exposure Analysis")

st.markdown("""
This section analyzes customer concentration, revenue contribution,
and churn exposure across geographic regions.
Designed to support regional strategy and resource allocation decisions.
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
st.sidebar.header("🔎 Geographic Filters")

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["contract"].unique(),
    default=df["contract"].unique()
)

churn_filter = st.sidebar.multiselect(
    "Churn Label",
    options=df["churn_label"].unique(),
    default=df["churn_label"].unique()
)

filtered_df = df[
    (df["contract"].isin(contract_filter)) &
    (df["churn_label"].isin(churn_filter))
]

# ======================================================
# KPI SECTION
# ======================================================
st.subheader("📌 Regional Performance Indicators")

total_revenue = filtered_df["total_revenue"].sum()
total_customers = filtered_df["customer_id"].nunique()
avg_cltv = filtered_df["cltv"].mean()
avg_churn_rate = filtered_df["churn_value"].mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Customers", f"{total_customers:,}")
col3.metric("Average CLTV", f"${avg_cltv:,.0f}")
col4.metric("Avg Churn Rate", f"{avg_churn_rate:.2f}%")

st.divider()

# ======================================================
# TOP STATES BY REVENUE
# ======================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 States by Revenue")

    revenue_state = (
        filtered_df.groupby("state")["total_revenue"]
        .sum()
        .reset_index()
        .sort_values(by="total_revenue", ascending=False)
        .head(10)
    )

    fig_revenue = px.bar(
        revenue_state,
        x="state",
        y="total_revenue"
    )

    st.plotly_chart(fig_revenue, use_container_width=True)

with col2:
    st.subheader("Churn Rate by State (Top 10 by Customers)")

    churn_state = (
        filtered_df.groupby("state")
        .agg(
            customers=("customer_id", "count"),
            churn_rate=("churn_value", "mean")
        )
        .reset_index()
        .sort_values(by="customers", ascending=False)
        .head(10)
    )

    churn_state["churn_rate"] = churn_state["churn_rate"] * 100

    fig_churn = px.bar(
        churn_state,
        x="state",
        y="churn_rate"
    )

    st.plotly_chart(fig_churn, use_container_width=True)

st.divider()

# ======================================================
# GEO SCATTER MAP
# ======================================================
st.subheader("Customer Geographic Distribution")

fig_map = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="churn_label",
    size="monthly_charges",
    hover_data=[
        "state",
        "city",
        "contract",
        "cltv"
    ],
    zoom=3,
    height=600
)

fig_map.update_layout(mapbox_style="carto-positron")

st.plotly_chart(fig_map, use_container_width=True)

st.divider()

# ======================================================
# CLTV DISTRIBUTION BY STATE
# ======================================================
st.subheader("CLTV Distribution by State (Top 10 Revenue States)")

top_states = revenue_state["state"].tolist()

cltv_state = filtered_df[filtered_df["state"].isin(top_states)]

fig_cltv = px.box(
    cltv_state,
    x="state",
    y="cltv"
)

st.plotly_chart(fig_cltv, use_container_width=True)

st.divider()

# ======================================================
# STRATEGIC INSIGHT
# ======================================================
st.subheader("📌 Regional Strategy Insights")

st.markdown("""
- Revenue concentration is heavily clustered in specific high-density states.
- Some high-revenue states simultaneously exhibit elevated churn exposure.
- Geographic churn clustering indicates localized service or pricing sensitivity.
- CLTV variability across regions suggests targeted retention campaigns.
- Regional prioritization can optimize retention investment allocation.
""")

st.caption("Customer Churn Intelligence Dashboard – Geographic & Revenue Mapping")
