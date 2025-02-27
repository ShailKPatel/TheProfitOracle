import streamlit as st

# =========================================
# 🏛️ Streamlit Multi-Page Application Setup
# =========================================

# Define distinct sections of the application, ensuring modularity and ease of navigation.
home_page = st.Page("pages/Dashboard_Home.py", icon='🏠')  # Primary landing interface
data_analysis_module = st.Page("pages/Data_Analysis_Module.py", icon='🔬')  # Core analytical functionalities
development_credits = st.Page("pages/Development_Credits.py", icon='🧠')  # Acknowledgments and team contributions
technological_framework = st.Page("pages/Technological_Framework.py", icon='🛠️')  # Libraries, dependencies, and system architecture

# =========================================
# 🧭 Navigation Configuration
# =========================================

# Initialize the navigation system with clearly delineated pages
navigation_controller = st.navigation(
    [home_page, data_analysis_module, development_credits, technological_framework]
)

# =========================================
# 🚀 Application Execution
# =========================================

if __name__ == "__main__":
    navigation_controller.run()
