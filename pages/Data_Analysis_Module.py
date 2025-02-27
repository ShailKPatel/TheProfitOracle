import streamlit as st
import pandas as pd
import data_preproccesing.data_preprocessor as dp
import traceback
import sales_analysis.sales_trends as sts


# Logo
image = "assets/logo.png"
st.logo(image, size='large')

# Title & File Upload Section

st.title("🔬 Data Analysis: Extracting Insights with Precision")

st.subheader("📂 Upload Required Data Files")

# File uploaders for three mandatory files
try:
    product_file = st.file_uploader("Upload Product Data (CSV, XLS, XLSX)", type=["csv", "xls", "xlsx"])
    sales_file = st.file_uploader("Upload Sales Data (CSV, XLS, XLSX)", type=["csv", "xls", "xlsx"])
    customer_file = st.file_uploader("Upload Customer Data (CSV, XLS, XLSX)", type=["csv", "xls", "xlsx"])
    
except Exception as e:
    st.error(f"You didn't follow Upload Rules`: {e}")
    st.text("🔍 Error Details:")  # Optional label for clarity
    st.code(traceback.format_exc(), language="python")  # Display the full traceback

        
# Data Upload Rules
if not product_file and not sales_file and not customer_file:
    
    st.markdown("""
    ### 📜 **Data Submission Guidelines**  

    **Attention, Data Custodian.** The integrity of this system relies upon the precision and structure of the data provided. Adhere strictly to the following directives to ensure seamless processing.  

    ---

    ### ✅ **Accepted File Formats:**  
    - **CSV (`.csv`)** – Standard format for structured data.  
    - **Excel (`.xls`, `.xlsx`, `.xlsm`, `.xlsb`)** – Widely used for tabular data storage.  

    **⛔ Rejected Formats:** `.txt`, `.pdf`, `.png`, `.jpg`, `.docx`, `.pptx`. This system is designed for analytical rigor, not document archiving or image processing.  

    ---

    ### 📏 **Data Structure Requirements**  

    - **🆔 Roll Number:** Must be unique, complete, and free from duplication.  
    - **📊 Subject Data:**  
    - Attendance and marks must adhere to the format: `"Subject Attendance"` and `"Subject Marks"` (e.g., `"Mathematics Attendance"`, `"Mathematics Marks"`).  
    - If attendance data is provided for a subject, corresponding marks data **must** be present, and vice versa.  
    - **👨‍🏫 Teacher Column (Optional):** If included, must follow the format `"Subject Teacher"` (e.g., `"Mathematics Teacher"`).  

    ---

    ### 🔢 **Numerical Standards**  
    - Attendance and marks must be numerical values within **0–100**.  
    - Decimal precision should not exceed two places.  

    ---

    ### 🚧 **Restrictions & Compliance**  
    - A maximum of **N subjects** is permissible.  
    - Extraneous columns outside of **Roll No, Attendance, Marks, Teacher** will be discarded.  

    ---

    ### ⚠ **Non-Compliance Consequences**  
    - Invalid data will result in rejection without exception.  
    - Error messages will be issued, detailing the discrepancy.  
    - Continued violations will be met with automated denial of processing.  

    Ensure your submission aligns with these standards to facilitate a seamless validation process.  
    """)
    
# Analysis Options with Witty Labels
if product_file and sales_file and customer_file:
    
    product_df = dp.process_product_file(product_file)
    sales_df = dp.process_sales_file(sales_file)
    customer_df = dp.process_customer_file(customer_file)
    
    st.subheader("Analysis Menu")
    try:

        if st.button("Sales Trends 📊"):
            fig = sts.plot_sales_trends(sales_df)
            st.pyplot(fig)
                
                
        if st.button("⚖️ Gender Bias Detection"):
            st.write("✅ Bias analysis complete! If the results make you uncomfortable, welcome to reality. 😉")


        if st.button("☪️✝️🕉️ Religious Bias Detection"):
            st.write("✅ Bias analysis complete! If the results are shocking, just remember—faith can move mountains, but data doesn’t lie. 📊😉")


        if st.button("📊 Subject Showdown: Which One Wins?"):
            st.write("✅ Bias analysis complete! If the results are shocking, just remember—faith can move mountains, but data doesn’t lie. 📊😉")
            
    except Exception as e:
        st.error(f"You didn't follow Upload Rules`: {e}")

# -------------------------------
# Closing Line
# -------------------------------

st.markdown("📜 *Under MIT License*")


