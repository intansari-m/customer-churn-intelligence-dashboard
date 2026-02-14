# 📊 Customer Churn Intelligence Dashboard (Streamlit App)

An end-to-end **Business Intelligence dashboard** built with **Streamlit** to monitor customer stability, quantify revenue exposure, and support **data-driven retention strategies**.

🔗 **Live App**  
https://intansari-customer-churn-intelligence-dashboard.streamlit.app/

---

## 🚀 Project Overview

Customer churn directly impacts recurring revenue stability. Losing high-value customers is more costly than retaining them.  

This platform aims to:

- Monitor high-risk customer segments  
- Analyze service adoption & churn drivers  
- Quantify financial exposure  
- Simulate potential revenue recovery  
- Provide interactive executive dashboards  

It combines **risk modeling, CLTV analysis, and BI visualization** in a single interactive system.

---

## 🎯 Key Objectives

- Identify high-risk customers proactively  
- Evaluate contract-based stability  
- Detect service-level churn drivers  
- Quantify financial exposure  
- Simulate retention scenarios  
- Translate analytics into actionable strategies  

---

## 🧠 Analytical Strategy

The dashboard leverages:

- Historical customer data for segmentation & CLTV estimation  
- Behavioral & service-level features for churn risk scoring  
- Risk tiering based on CLTV and retention priority  
- Interactive dashboarding for scenario simulation and executive decision support  

Final outputs support **strategic retention prioritization** and **revenue protection**.

---

## ⚖️ Risk & Retention Tier Strategy

Churn risk is segmented using probabilistic scoring:

| Retention Priority | Description |
|------------------|-------------|
| 🔴 Critical Retention | High CLTV + High Risk |
| 🟡 High Value - Monitor | High CLTV, moderate risk |
| 🟢 Standard | Other customers |

This ensures **business action is prioritized toward high-value, high-risk segments**.

---

## 📊 Application Features

### 1️⃣ Executive Overview
- KPI summary (total customers, churned customers, churn rate, total revenue, average CLTV)  
- Churn distribution by contract and customer status  
- Revenue & tenure insights  
- Executive-level strategic insights

### 2️⃣ Customer & Revenue Analysis
- Revenue contribution by payment method & internet service  
- CLTV and monthly charges segmentation  
- Scatter analysis: tenure vs CLTV  
- Revenue & customer segmentation insights

### 3️⃣ Churn Risk Deep Dive
- Behavioral & service-level churn analysis  
- Satisfaction vs churn visualization  
- Online security & tech support impact on churn  
- Churn category & score distribution  
- Actionable behavioral insights

### 4️⃣ Geographic Intelligence
- Regional revenue & churn analysis  
- Top states by revenue & churn rate  
- CLTV distribution by region  
- Interactive geographic scatter map  
- Strategic regional insights

### 5️⃣ CLTV & Retention Strategy
- CLTV vs churn score scatter matrix  
- Retention priority distribution  
- Revenue by retention segment  
- Contract impact analysis  
- Strategic retention recommendations

### 6️⃣ Tableau Dashboard Showcase
- Executive BI dashboards for reporting & storytelling  
- Visualization for churn, revenue, and geographic intelligence  
- Complementary to interactive Streamlit app

### 7️⃣ About Me
- Analyst profile and experience  
- Technical skills (Python, SQL, Pandas, NumPy, Streamlit, Plotly, Tableau, Scikit-learn)  
- Contact links: Email, LinkedIn, WhatsApp, GitHub  

---

## 🗂️ Project Structure

```text
customer-churn-intelligence-dashboard/
├── app.py                       # Main Streamlit entry point
├── pages/
│   ├── 1_📊_Executive_Overview.py
│   ├── 2_👥_Customer_Revenue_Analysis.py
│   ├── 3_⚠️_Churn_Risk_Deep_Dive.py
│   ├── 4_🌍_Geographic_Intelligence.py
│   ├── 5_📈_CLTV_Retention_Strategy.py
│   ├── 6_📊_Tableau_Dashboard_Showcase.py
│   └── 7_👤_About_Me.py
├── data/
│   └── final_dataset.csv
├── images/
│   ├── Dashboard_1.png
│   ├── Dashboard_2.png
│   ├── Dashboard_3.png
│   └── FOTO_INTAN.png
├── requirements.txt
└── README.md
```

---
## 🛠️ Tools & Technologies

- Python  
- Pandas & NumPy  
- Plotly  
- Streamlit  
- Tableau (optional)  
- Interactive Dashboards & Revenue Risk Modeling

---

## 📌 Business Value

This dashboard enables organizations to:

- Detect high-risk customers proactively  
- Monitor revenue exposure by segment & region  
- Prioritize retention resources effectively  
- Support executive decision-making with data transparency  
- Translate analytics into actionable strategies

---

## 👤 Author

**Intan Sari Muharni**  
Data Analyst | Aspiring Data Scientist  

<p align="left">
  <a href="mailto:intansariarni@gmail.com">
    <img src="https://img.icons8.com/color/48/gmail-new.png" width="32"/>
  </a>
  <a href="https://www.linkedin.com/in/intan-sari-muharni" target="_blank">
    <img src="https://img.icons8.com/color/48/linkedin.png" width="32"/>
  </a>
  <a href="https://github.com/intansari-m" target="_blank">
    <img src="https://img.icons8.com/glyph-neue/64/github.png" width="32"/>
  </a>
  <a href="https://wa.me/6285717595056" target="_blank">
    <img src="https://img.icons8.com/color/48/whatsapp.png" width="32"/>
  </a>
</p>

---

## ✅ Status

🚀 **Deployed & Production-Ready**  

This project demonstrates a complete end-to-end **Business Intelligence workflow**, from data ingestion, dashboarding, segmentation, revenue analysis, to interactive deployment.
