import streamlit as st
import os

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="About Me",
    page_icon="👤",
    layout="wide"
)

# ======================
# HERO SECTION
# ======================
st.title("👤 About Me")
st.divider()

col1, col2 = st.columns([1, 3])

with col1:
    image_path = os.path.join("images", "FOTO_INTAN.png")
    st.image(
        image_path,
        width=280  
    )

with col2:
    st.markdown("""
    ## Intan Sari Muharni  
    **Data Analyst | Aspiring Data Scientist**

    Industrial Engineering graduate with strong experience in  
    **data analysis, process optimization, and business-driven analytics**.

    I specialize in transforming raw data into **actionable insights**,  
    building **end-to-end analytics solutions**, and translating technical findings  
    into clear business recommendations.
    """)

st.divider()

# ======================
# WHAT I DO
# ======================
st.subheader("🎯 What I Do")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ✔ Build interactive **business dashboards**  
    ✔ Perform **EDA & customer segmentation**  
    ✔ Conduct statistical analysis & hypothesis testing  
    """)

with col2:
    st.markdown("""
    ✔ Develop **machine learning models**  
    ✔ Translate data into strategic insights  
    ✔ Deploy analytics solutions using Streamlit  
    """)

st.divider()

# ======================
# EXPERIENCE
# ======================
st.subheader("💼 Experience Highlights")

st.markdown("""
### R&D Packaging Development Staff  
**PT Pharos Indonesia**

- Reduced material waste by **12%** through production data analysis  
- Improved operational efficiency by **15%**  
- Delivered analytical reports to support management decisions  
- Collaborated cross-functionally with Marketing & Production  
""")

st.divider()

# ======================
# TECHNICAL SKILLS
# ======================
st.subheader("🛠️ Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Programming**
    - Python  
    - SQL  
    - Pandas  
    - NumPy  
    """)

with col2:
    st.markdown("""
    **Visualization**
    - Streamlit  
    - Plotly  
    - Tableau  
    - Power BI  
    """)

with col3:
    st.markdown("""
    **Machine Learning**
    - Scikit-learn  
    - Classification Models  
    - Model Evaluation  
    - Feature Engineering  
    """)

st.divider()

# ======================
# CONTACT
# ======================
st.subheader("📫 Let's Connect")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/732/732200.png",
        width=35
    )
    st.markdown("[Email](mailto:intansariarni@gmail.com)")

with c2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        width=35
    )
    st.markdown("[LinkedIn](https://www.linkedin.com/in/intan-sari-muharni)")

with c3:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/733/733585.png",
        width=35
    )
    st.markdown("[WhatsApp](https://wa.me/6285717595056)")

with c4:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/733/733553.png",
        width=35
    )
    st.markdown("[GitHub](https://github.com/intansari-m)")

st.divider()

st.success("🚀 Open to Data Analyst & Data Scientist opportunities.")
