# Sales Analysis and Prediction System Documentation

## 1. **Project Overview**
The **Sales Analysis and Prediction System** is a Python-based application that helps **small businesses** analyze and predict sales trends. It enables users to upload **sales, product, and customer data**, generating insightful visualizations, trend analyses, and predictions using **Machine Learning (Linear Regression, Multiple Linear Regression, and Clustering).**

### **Key Features**
- **Drag-and-Drop File Upload**: Upload sales data in CSV format.
- **Data Processing & Cleaning**: Handles missing values and converts necessary data types.
- **Statistical & Visual Analysis**:
  - Sales trends **(Daily, Weekly, Monthly Moving Averages)** using **Matplotlib & Plotly**.
  - Correlation Analysis between sales data.
- **Machine Learning Predictions**:
  - **Linear Regression & Multiple Linear Regression** for sales forecasting.
  - **Clustering Analysis** for customer segmentation.

---

## 2. **Project Structure**
```
SalesAnalysisSystem/
│   index.py
│   LICENSE
│   README.md
│   requirements.txt
│
├───assets
│       logo.png
│
├───data_preprocessing
│       data_preprocessor.py
│
├───pages
│       Dashboard_Home.py
│       Data_Analysis_Module.py
│       Technological_Framework.py
│       View_Review.py
│
├───prediction
│       linear_regression.py
│       sales_analysis.py
│
├───sales_analysis
│       location_profit.py
│       location_sales_analysis.py
│       profit_per_category.py
│       repeat_customers.py
│       sales_trends.py
│
└───tests
```

---

## 3. **Installation & Setup**
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

## 4. **Sales Analysis & Visualization**
### **Generating Sales Trends**
The system generates sales trends using **Matplotlib**. The `plot_sales_trends` function provides:
- **Daily Sales Trends** with a **7-day moving average**.
- **Weekly Sales Trends** with a **4-week moving average**.
- **Monthly Sales Trends** with a **3-month moving average**.

#### **Example Code:**
```python
import pandas as pd
from prediction.sales_analysis import plot_sales_trends

sales_df = pd.read_csv("tests/s3.csv")
fig = plot_sales_trends(sales_df)
fig.show()
```

---

## 5. **Machine Learning: Sales Prediction**
The system applies **Linear Regression** to predict future sales trends.

#### **Example Code:**
```python
from prediction.linear_regression import linear_regression_custom
predictions = linear_regression_custom(sales_df)
print(predictions)
```

---

## 6. **Common Errors & Fixes**
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
  cd SalesAnalysisSystem/
  python index.py
  ```

---

## 7. **License**
This project is open-source and available under the **MIT License**.

---

## 8. **Contributing**
Contributions are welcome! Feel free to fork this repo and submit a pull request.

### **Author:**
**Shail Patel**

---

### ⭐ **If you find this project helpful, don't forget to star the repository!** ⭐

