import streamlit as st
from PIL import Image

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Customer Intelligence & Retention Strategy Platform",
    page_icon="📊",
    layout="wide"
)

# ======================
# HERO SECTION
# ======================
st.title("📊 Customer Intelligence & Retention Strategy Platform")

st.markdown("""
A strategic Business Intelligence platform designed to monitor customer stability,
quantify revenue exposure, and support proactive retention decisions.

This dashboard reframes churn analysis from operational reporting
into executive-level financial risk management.
""")

st.divider()

# ======================
# BUSINESS CONTEXT
# ======================
st.header("📌 Business Context")

st.markdown("""
Customer churn directly impacts recurring revenue stability.  
Without proper monitoring, organizations face:

- Revenue volatility  
- Increasing acquisition costs  
- Unpredictable cash flow  
- Profit margin erosion  

Retention is not only a marketing issue —
it is a strategic financial priority.
""")

# ======================
# STRATEGIC RISK PERSPECTIVE
# ======================
st.header("📉 Strategic Risk Perspective")

st.markdown("""
Churn should be viewed as recurring revenue exposure.

If unmanaged, churn may:

- Reduce predictable revenue streams  
- Increase dependency on customer acquisition  
- Concentrate revenue among unstable segments  
- Undermine long-term profitability  

A proactive retention framework is essential for sustainable growth.
""")

# ======================
# PLATFORM OBJECTIVES
# ======================
st.header("🎯 Platform Objectives")

st.markdown("""
This platform is structured to:

- Identify high-risk customer segments  
- Evaluate contract-based stability  
- Detect service-level churn drivers  
- Quantify financial exposure  
- Simulate potential revenue recovery  

Each analytical module supports one core mission:  
**Revenue Protection & Retention Optimization**
""")

# ======================
# PLATFORM MODULES
# ======================
st.header("🧭 Platform Modules")

st.markdown("""
The system is organized into 7 analytical layers:

1️⃣ Executive Overview – KPI & retention summary  
   *(Content from 1_📊_Executive_Overview.py)*

2️⃣ Customer & Revenue Analysis – Demographic & revenue segmentation  
   *(Content from 2_👥_Customer_Revenue_Analysis.py)*

3️⃣ Churn Risk Deep Dive – Service adoption & churn drivers  
   *(Content from 3_⚠️_Churn_Risk_Deep_Dive.py)*

4️⃣ Geographic Intelligence – Regional revenue & churn mapping  
   *(Content from 4_🌍_Geographic_Intelligence.py)*

5️⃣ CLTV & Retention Strategy – Scenario-based retention modeling  
   *(Content from 5_📈_CLTV_Retention_Strategy.py)*

6️⃣ Tableau Dashboard Showcase – Executive BI visualization layer  
   *(Content from 6_📊_Tableau_Dashboard_Showcase.py)*

7️⃣ About Me – Project & analyst profile  
   *(Content from 7_👤_About_Me.py)*

This layered structure mirrors professional Business Intelligence architecture.
""")

# ======================
# DASHBOARD PREVIEW
# ======================
st.header("📷 Dashboard Preview")

try:
    image = Image.open("images/Dashboard_1.png")
    st.image(image, use_container_width=True)
except:
    st.info("Preview image not available.")

# ======================
# TECHNOLOGY STACK
# ======================
st.header("🛠️ Technology Stack")

st.markdown("""
- Python  
- Pandas & NumPy  
- Plotly  
- Streamlit  
- Tableau  

Combining analytical rigor with executive visualization
ensures both technical depth and business clarity.
""")

st.divider()

st.success("👉 Use the sidebar to explore each strategic module.")
