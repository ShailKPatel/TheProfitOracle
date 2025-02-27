import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linear_regression import linear_regression  # Correct import

def predict_quantity_sold(sales_df, ax):
    """
    Predicts 'Quantity_Sold' using 'Sales_Price' based on Linear Regression.

    Parameters:
    - sales_df (pd.DataFrame): DataFrame containing 'Sales_Price' and 'Quantity_Sold'.
    - ax (matplotlib.axes._axes.Axes): The subplot axis to draw the graph on.

    Returns:
    - None (Plots directly on ax)
    """

    # Clean data: Remove NaN and ensure correct type
    sales_df = sales_df.dropna(subset=["Sales_Price", "Quantity_Sold"])
    X = pd.to_numeric(sales_df["Sales_Price"], errors="coerce").values
    y = pd.to_numeric(sales_df["Quantity_Sold"], errors="coerce").values

    # Normalize inputs to prevent overflow
    X_mean, X_std = np.mean(X), np.std(X)
    y_mean, y_std = np.mean(y), np.std(y)

    if X_std == 0 or y_std == 0:
        ax.text(0.5, 0.5, "Data issue: Zero variance", ha="center", va="center", fontsize=12)
        return

    X_norm = (X - X_mean) / X_std
    y_norm = (y - y_mean) / y_std

    # Train the model
    w_norm, b_norm = linear_regression(X_norm, y_norm, learning_rate=0.001, epochs=10000)

    # Convert back to original scale
    w = w_norm * (y_std / X_std)
    b = (b_norm * y_std) + y_mean - w * X_mean

    # Generate predictions
    X_range = np.linspace(X.min(), X.max(), 100)
    y_pred = w * X_range + b

    # Scatter plot of actual data
    ax.scatter(X, y, label="Actual Data", color="blue", alpha=0.6)
    ax.plot(X_range, y_pred, label=f"y = {w:.2f}x + {b:.2f}", color="red", linewidth=2)

    # Labels and title
    ax.set_xlabel("Sales Price")
    ax.set_ylabel("Quantity Sold")
    ax.set_title("Sales Price vs Quantity Sold")
    ax.legend()
    ax.grid(True)


def correlation_matrix(sales_df, products_df, customers_df, ax):
    """
    Generates a correlation matrix for Quantity_Sold, Sales_Price, Price, and Age.
    
    Parameters:
    - sales_df (pd.DataFrame)
    - products_df (pd.DataFrame)
    - customers_df (pd.DataFrame)
    - ax (matplotlib.axes._axes.Axes): The subplot axis to draw the heatmap on.

    Returns:
    - None (Plots directly on ax)
    """

    # Merge datasets
    merged_df = sales_df.merge(products_df[["PID", "Price"]], on="PID", how="left")
    merged_df = merged_df.merge(customers_df[["CID", "Age"]], on="CID", how="left")

    # Select relevant numerical columns
    correlation_data = merged_df[["Quantity_Sold", "Sales_Price", "Price", "Age"]].dropna()

    if correlation_data.empty:
        ax.text(0.5, 0.5, "No valid correlation data", ha="center", va="center", fontsize=12)
        return

    # Compute correlation matrix
    corr_matrix = correlation_data.corr()

    # Plot heatmap
    cax = ax.matshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(cax, ax=ax)

    # Set axis labels
    ax.set_xticks(range(len(corr_matrix.columns)))
    ax.set_yticks(range(len(corr_matrix.columns)))
    ax.set_xticklabels(corr_matrix.columns, rotation=45, ha="left")
    ax.set_yticklabels(corr_matrix.columns)
    ax.set_title("Correlation Matrix", pad=20)

    # Display correlation values
    for i in range(len(corr_matrix.columns)):
        for j in range(len(corr_matrix.columns)):
            ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha="center", va="center", color="black")


def generate_combined_figure(sales_df, products_df, customers_df):
    """
    Generates a single figure with two subplots: 
    1. Scatter plot of 'Sales_Price' vs 'Quantity_Sold' with a regression line.
    2. Heatmap of the correlation matrix.

    Parameters:
    - sales_df (pd.DataFrame)
    - products_df (pd.DataFrame)
    - customers_df (pd.DataFrame)

    Returns:
    - matplotlib.figure.Figure
    """

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Call individual plotting functions
    predict_quantity_sold(sales_df, axes[0])
    correlation_matrix(sales_df, products_df, customers_df, axes[1])

    fig.tight_layout()
    return fig


# === Example Usage ===
if __name__ == "__main__":
    # Load test data
    sales_df = pd.read_csv("tests/s3.csv")
    products_df = pd.read_csv("tests/p3.csv")
    customers_df = pd.read_csv("tests/c3.csv")

    # Convert columns to numeric
    sales_df["Sales_Price"] = pd.to_numeric(sales_df["Sales_Price"], errors="coerce")
    sales_df["Quantity_Sold"] = pd.to_numeric(sales_df["Quantity_Sold"], errors="coerce")
    products_df["Price"] = pd.to_numeric(products_df["Price"], errors="coerce")
    customers_df["Age"] = pd.to_numeric(customers_df["Age"], errors="coerce")

    # Generate the final combined figure
    fig = generate_combined_figure(sales_df, products_df, customers_df)
    plt.show()
