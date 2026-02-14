import streamlit as st
from pathlib import Path

# ======================================================
# PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="Tableau Dashboard Showcase",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Tableau Business Intelligence Dashboard")
st.markdown("### Visual Storytelling & Executive Reporting Layer")

st.markdown("""
In addition to the interactive Streamlit application,
this project also includes a Tableau-based executive dashboard
designed for structured BI reporting and stakeholder presentation.
""")

st.divider()

# ======================================================
# LOAD IMAGES
# ======================================================
base_path = Path(__file__).resolve().parent.parent
image_path = base_path / "images"

st.subheader("Executive Overview Dashboard")
st.image(str(image_path / "Dashboard_1.png"), use_container_width=True)

st.subheader("Churn Risk & Service Analysis")
st.image(str(image_path / "Dashboard_2.png"), use_container_width=True)

st.subheader("Revenue & Geographic Intelligence")
st.image(str(image_path / "Dashboard_3.png"), use_container_width=True)

st.divider()

# ======================================================
# STRATEGIC CONTEXT
# ======================================================
st.subheader("📌 Why Two Dashboard Approaches?")

st.markdown("""
**Tableau Dashboard**
- Designed for executive presentation
- Structured and storytelling-driven
- Suitable for BI reporting workflows

**Streamlit Application**
- Interactive and filter-driven exploration
- Dynamic segmentation capability
- Advanced analytical flexibility

This dual-approach demonstrates both BI visualization capability
and data application development skills.
""")

st.caption("Customer Churn Intelligence Project – BI & Application Integration")
