import streamlit as st
import data_preproccesing.data_preprocessor as dp
import sales_analysis.sales_trends as sts
import sales_analysis.repeat_customers as rc
import sales_analysis.profit_per_category as ppc
import sales_analysis.location_sales_analysis as lsa
import sales_analysis.location_profit as lp
import prediction.sales_analysis as sa

# Logo
image = "assets/logo.png"
st.logo(image, size='large')

# Title & File Upload Section

st.title("🔬 Data Analysis: Extracting Insights with Precision")

st.subheader("📂 Upload Required Data Files")
product_file = None
sales_file = None
customer_file = None

# File uploaders for three mandatory files
try:
    product_file = st.file_uploader("Upload Product Data (CSV, XLS, XLSX)", type=["csv", "xls", "xlsx"])
    sales_file = st.file_uploader("Upload Sales Data (CSV, XLS, XLSX)", type=["csv", "xls", "xlsx"])
    customer_file = st.file_uploader("Upload Customer Data (CSV, XLS, XLSX)", type=["csv", "xls", "xlsx"])
    
except Exception as e:
    st.error(f"You didn't follow Upload Rules`: {e}.\nTry Restaring reloading the page.")

        
# Data Upload Rules
if not( product_file and sales_file and customer_file):
    
    st.markdown("""
    ### 📜 **Data Submission Guidelines**  

    **Attention, Business Analyst.** The accuracy and reliability of TheProfitOracle depend on properly structured data. Follow these guidelines to ensure smooth processing.  

    ---

    ### ✅ **Accepted File Formats:**  
    - **CSV (`.csv`)** – Recommended for structured data.  
    - **Excel (`.xls`, `.xlsx`)** – Supported for tabular data.  

    **⛔ Rejected Formats:** `.txt`, `.pdf`, `.png`, `.jpg`, `.docx`, `.pptx`. This tool is designed for numerical and structured business data analysis.  

    ---

    ### 📏 **Data Structure Requirements**  

    #### ** Mandatory Files**  
    - **Products Data** (`PID`, `Name`, `Description`, `Price`, etc.)  
    - **Sales Data** (`Time`, `Date`, `CID`, `Quantity`, `SID`, `Sales Price`, `Location`, etc.)  
    - **Customers Data** (`CID`, `Age`, `Gender`, etc.)  

    Each file must follow the correct structure, and column names should be consistent.  

    ---

    ### 🔢 **Numerical Standards**  
    - Sales prices and quantities must be **positive numerical values**.  
    - Dates must follow the format **YYYY-MM-DD** for consistency.  

    ---

    ### 🚧 **Restrictions & Compliance**  
    - Ensure **no missing values** in mandatory fields.  
    - Unique identifiers (`PID`, `CID`, `SID`) should not have duplicates.  

    ---

    ### ⚠ **Non-Compliance Consequences**  
    - Incorrect data formats will result in **automatic rejection**.  
    - Errors will be flagged with **detailed messages**.  
    - Continuous violations may lead to **denial of processing**.  

    Align your submission with these standards to enable accurate business insights and predictions.  


    ### ⚠ **Non-Compliance Consequences**  
    - Invalid data will result in rejection without exception.  
    - Error messages will be issued, detailing the discrepancy.  
    - Continued violations will be met with automated denial of processing.  

    Ensure your submission aligns with these standards to facilitate a seamless validation process.  
    """)
    
try:
    # Analysis Options with Witty Labels
    if product_file and sales_file and customer_file:
        
        product_df = dp.process_product_file(product_file)
        sales_df = dp.process_sales_file(sales_file)
        customer_df = dp.process_customer_file(customer_file)
        
        st.subheader("Analysis Menu")

        if st.button("Sales Trends 📊"):
            fig = sts.plot_sales_trends(sales_df)
            st.pyplot(fig)


        if st.button("Reapeat Customers🔁"):
            repeat_customer_df, fig = rc.analyze_repeat_customers(sales_df)
            st.dataframe(repeat_customer_df, use_container_width=True, hide_index=True)
            st.pyplot(fig)


        if st.button("Categorywise profit💵"):
            fig = ppc.analyze_profit_per_category(sales_df, product_df)
            st.pyplot(fig)


        if st.button("Sales Location analysis🗺"):
            fig = lsa.analyze_sales_by_location(sales_df, customer_df)
            st.pyplot(fig)
                
                
        if st.button("Locationwise Profit📊"):
            fig = lp.analyze_category_and_profit(sales_df, product_df)
            st.pyplot(fig)
                
                
        if st.button("Sales Analysis📶"):
            fig = sa.generate_combined_figure(sales_df, product_df, customer_df)
            st.pyplot(fig)

            
except Exception as e:
    st.error(f"You didn't follow Upload Rules`: {e}.\nTry Restaring reloading the page.")

# Closing Line
st.markdown("📜 *Under MIT License*")