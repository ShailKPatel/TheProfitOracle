import streamlit as st

# =========================================
# 🏛️ Business Insights Dashboard - Home Page
# =========================================

# Load and display the company logo
logo_path = "assets/company_logo.png"  # Ensure the correct path to your logo
st.logo(logo_path, size='large')

# -------------------------------
# 📊 Project Introduction
# -------------------------------

st.title("📈 RapidBiz Insights 🚀")

st.markdown("""
_A powerful yet effortless analytical tool designed for small business owners and managers._  
**Upload your sales and product data** to instantly receive actionable insights, trends, and forecasts.
""")

# -------------------------------
# 🔍 System Overview
# -------------------------------

st.header("🔎 Why Choose RapidBiz Insights?")
st.write("""
In today's fast-paced business environment, data-driven decision-making is critical.  
However, small businesses often lack dedicated analysts. **RapidBiz Insights** bridges this gap  
by providing automated, intelligent analysis at the click of a button.  
""")

# -------------------------------
# ✨ Key Features
# -------------------------------

st.header("✨ Core Functionalities")
st.markdown("""
✔ **Effortless File Upload**: Drop in **CSV** or **Excel** files—no manual data entry required.  
✔ **Sales Performance Analysis**: Identify **top-selling products**, revenue trends, and seasonal patterns.  
✔ **Customer Demographics Insights**: Understand your customer base with **age, gender, and buying trends**.  
✔ **Market Segmentation & Clustering**: Group customers based on purchasing behavior.  
✔ **Predictive Sales Forecasting**: Leverage **machine learning** (Linear Regression, Clustering) to predict sales.  
✔ **Dynamic Data Visualization**: Interactive **Plotly charts** for enhanced insights.  
✔ **Error Detection & Data Cleaning**: Ensures data integrity by handling missing values and inconsistencies.  
""")

# -------------------------------
# 📌 Navigation Links
# -------------------------------

st.header("🚀 Explore RapidBiz Insights")

with st.container(border=True):
    """ # 🔬 Data Analysis Module
    Upload your files and receive detailed business insights."""
    st.page_link("pages/Data_Analysis_Module.py", label="Go to Data Analysis", icon="📊")

with st.container(border=True):
    """ # 🧠 Team & Acknowledgments
    Learn about the contributors behind this project."""
    st.page_link("pages/Development_Credits.py", label="View Contributors", icon="🧑")

with st.container(border=True):
    """ # 🛠️ Technological Framework
    Discover the technologies powering this system."""
    st.page_link("pages/Technological_Framework.py", label="View Technologies", icon="⚙️")

# -------------------------------
# 📜 Footer
# -------------------------------

st.markdown("---")
st.markdown("📜 **MIT Licensed** | 🚀 Empowering Small Businesses with Data-Driven Decisions")
