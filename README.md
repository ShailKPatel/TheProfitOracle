# Sales Analysis and Prediction System

## 📌 **Project Overview**
The **Sales Analysis and Prediction System** is a Python-based tool designed for **small businesses** to analyze and forecast sales trends. It allows users to upload **sales, product, and customer data** and generates insightful visualizations, trend analysis, and predictions using **Machine Learning (Linear Regression, Multiple Linear Regression, and Clustering).**

### 🔹 **Key Features**
- **Drag-and-Drop File Upload**: Users can upload sales data in CSV format.
- **Mandatory & Optional Files**:
  - **Products File (Mandatory)** – Contains product details (`PID`, `Name`, `Description`, `Price`, etc.).
  - **Sales File (Mandatory)** – Contains sales transaction data (`Time`, `Date`, `CID`, `Quantity`, `SID`, `Sales Price`, `Location`, etc.).
  - **Customers File (Optional)** – Contains customer details (`CID`, `Age`, `Gender`, etc.).
- **Data Processing & Cleaning**: Handles missing values and converts necessary data types.
- **Statistical & Visual Analysis**:
  - Correlation Analysis between **Attendance, Theory, and Practical Marks**.
  - Sales Trends **(Daily, Weekly, and Monthly Moving Averages)** using **Matplotlib & Plotly**.
- **Machine Learning Predictions**:
  - **Linear Regression & Multiple Linear Regression** for sales forecasting.
  - **Clustering Analysis** for customer segmentation.

---

## 📁 **Project Structure**
```
TheProfitOracle/
│── index.py                      # Main script to run the application
│── Data_Analysis_Module.py        # Handles data analysis & visualization
│── prediction/
│   │── __init__.py                # Makes 'prediction' a package
│   │── sales_analysis.py           # Performs sales trend analysis
│   │── linear_regression.py        # Implements ML-based sales forecasting
│── tests/
│   │── p3.csv                      # Sample Product File
│   │── s3.csv                      # Sample Sales File
│   │── c2.csv                      # Sample Customer File
│── requirements.txt                # List of dependencies
│── README.md                       # Project documentation
```

---

## 🔧 **Installation & Setup**
### **1️⃣ Install Python & Dependencies**
Ensure you have **Python 3.10+** installed. Then, install dependencies:
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Application**
Navigate to the project folder and run:
```bash
python index.py
```

---

## 📊 **Sales Analysis & Visualization**
The system generates sales trends using **Matplotlib**. The `plot_sales_trends` function:
1. **Daily Sales Trends** with a **7-day moving average**.
2. **Weekly Sales Trends** with a **4-week moving average**.
3. **Monthly Sales Trends** with a **3-month moving average**.

**Example Code:**
```python
import pandas as pd
from prediction.sales_analysis import plot_sales_trends

sales_df = pd.read_csv("tests/s3.csv")
fig = plot_sales_trends(sales_df)
fig.show()
```

---

## 🧠 **Machine Learning: Linear Regression for Sales Prediction**
The system applies **Linear Regression** to predict future sales trends.

**Example Code:**
```python
from prediction.linear_regression import linear_regression_custom
predictions = linear_regression_custom(sales_df)
print(predictions)
```

---

## ❗ **Common Errors & Fixes**
### **1️⃣ `ModuleNotFoundError: No module named 'linear_regression'`**
#### **Fix:**
- Ensure `linear_regression.py` exists in the `prediction/` folder.
- Try **relative import** inside `sales_analysis.py`:
  ```python
  from .linear_regression import linear_regression_custom
  ```
- Add the folder to `sys.path`:
  ```python
  import sys, os
  sys.path.append(os.path.abspath(os.path.dirname(__file__)))
  ```
- Run the script from the correct directory:
  ```bash
  cd M:\TheProfitOracle\
  python index.py
  ```

---

## 📜 **License**
This project is open-source and available under the **MIT License**.

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to fork this repo and submit a pull request.

### **Author:**
**Shail Patel**

---

### ⭐ **If you find this project helpful, don't forget to star the repository!** ⭐

