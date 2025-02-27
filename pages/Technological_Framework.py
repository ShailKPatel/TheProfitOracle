import streamlit as st

# Logo
image = "assets/logo.png"
st.logo(image, size='large')

# Page Title
st.title("🔹 Technical Overview")

st.write("This project leverages data processing and visualization techniques to extract meaningful insights from sales data.")

# -------------------------------
# 🔹 Core Technologies
# -------------------------------

st.subheader("📌 **Technology Stack**")
st.write(
    "**📝 Programming Language:** Python\n"
    "**🎨 Framework:** Streamlit (For interactive web-based visualization)\n"
    "**📚 Libraries Used:**"
)

st.markdown(
    """
    - **NumPy & Pandas** – Fundamental for efficient data handling and manipulation.
    - **Matplotlib** – Used for generating clear and informative visualizations.
    """
)

# -------------------------------
# 🔹 Data Processing and Analysis
# -------------------------------

st.subheader("📊 **Data Processing & Visualization**")
st.markdown(
    """
    - **Data Cleaning & Transformation** – Utilizing Pandas for structured data preprocessing.
    - **Statistical Summaries** – Extracting insights through descriptive statistics.
    - **Graphical Representation** – Leveraging Matplotlib to visualize trends and distributions.
    """
)

# -------------------------------
# 🔹 Project Significance
# -------------------------------

st.subheader("📌 **Project Objective**")
st.write(
    "This system automates sales data analysis, providing businesses with structured reports and visual trends. "
    "By integrating NumPy, Pandas, and Matplotlib, it ensures efficient data handling and effective visualization."
)
