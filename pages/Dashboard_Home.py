import streamlit as st

# Sales Analysis & Prediction System

# Load and display the company logo
logo_path = "assets/logo.png"  # Ensure the correct path to your logo
st.logo(logo_path, size='large')

# Project Overview

st.title("📈 Sales Analysis & Prediction System")

st.markdown("""
This system provides automated sales analysis and forecasting for small businesses.  
By leveraging **data-driven insights**, it helps business owners optimize decision-making  
without requiring manual calculations or expertise in data science.
""")

# System Capabilities
st.header("🔎 System Features")

st.markdown("""
- **Automated Sales Performance Analysis**: Identify **top-selling products**, revenue trends, and demand fluctuations.
- **Customer Insights & Segmentation**: Analyze purchase patterns by **age, gender, and buying frequency**.
- **Predictive Modeling**: Forecast **future sales trends** using **Machine Learning (Regression & Clustering)**.
- **Data Quality Control**: Detect and handle **missing values, duplicate entries, and inconsistent records**.
- **Interactive Visualizations**: Generate **real-time analytics** with **Plotly-powered charts**.
""")

# Data Upload Requirements
st.header("📂 File Upload Guidelines")

st.markdown("""
To ensure accurate analysis, uploaded files must follow these guidelines:

### **1️⃣ Sales Data (Mandatory)**
- **File Format**: CSV or Excel  
- **Required Columns**:
  - `SID` (Sales Transaction ID) **[Unique]**
    - `Date`, `Time`
    - `PID` (Product ID)
    - `CID` (Customer ID) _(If unavailable, use `0`)_
    - `Quantity_Sold`
    - `Sales_Price`
    - `Location`

### **2️⃣ Product Data (Mandatory)**
- **File Format**: CSV or Excel  
- **Required Columns**:
  - `PID` (Product ID) **[Unique]**
    - `Product_Name`
    - `P_Description`
    - `Manufacturing_Cost`
    - `Category`

### **3️⃣ Customer Data **
- **File Format**: CSV or Excel  
- **Required Columns**:
  - `CID` (Customer ID) **[Unique]**
    - `Age` _(Valid range: `0 - 120`)_
    - `Gender` _(Accepted values: `"Male"`, `"Female"`, `"Trans"`)_

""")

# Navigation
st.header("🚀 System Modules")

with st.container(border=True):
    """ # 📊 Data Analysis
    Upload your files and generate insights automatically."""
    st.page_link("pages/Data_Analysis_Module.py", label="Go to Data Analysis", icon="📊")

with st.container(border=True):
    """ # 🏆 Contributors
    Meet the development team behind this system."""
    st.page_link("pages/Development_Credits.py", label="View Contributors", icon="👥")

with st.container(border=True):
    """ # 🛠️ Technology Stack
    Learn about the technologies powering this project."""
    st.page_link("pages/Technological_Framework.py", label="View Technologies", icon="⚙️")

# Legal & Licensing
st.markdown("---")
st.markdown("📜 **MIT Licensed** | Designed for Small Business Growth")
