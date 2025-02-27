import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_category_and_profit(sales_df, products_df):
    """
    Analyzes sales data to:
    1. Display the most popular product categories by location.
    2. Show profit per location using a Matplotlib heatmap.

    Parameters:
    - sales_df (pd.DataFrame): Contains 'Location', 'PID', 'Sales_Price'.
    - products_df (pd.DataFrame): Contains 'PID', 'Product_Name', 'P_Description', 'Price', 'Category'.

    Returns:
    - matplotlib.figure.Figure: A figure containing two subplots.
    """

    # === Step 1: Merge Sales Data with Product Data ===
    sales_with_products = sales_df.merge(products_df, on="PID", how="left")

    # === Step 2: Most Popular Categories by Location ===
    category_counts = sales_with_products.groupby(["Location", "Category"])["PID"].count().unstack().fillna(0)

    # === Step 3: Profit Calculation ===
    sales_with_products["Profit"] = sales_with_products["Sales_Price"] - sales_with_products["Price"]
    location_profit = sales_with_products.groupby("Location")["Profit"].sum().reset_index()

    # === Step 4: Plotting ===
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    plt.subplots_adjust(wspace=0.5)  # Increase spacing between subplots

    # === Plot 1: Most Popular Categories by Location ===
    category_colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#FFD700"]
    category_counts.plot(kind="bar", stacked=True, ax=axes[0], color=category_colors[:len(category_counts.columns)])

    axes[0].set_title("Most Popular Product Categories by Location", fontsize=14, fontweight="bold")
    axes[0].set_xlabel("Location", fontsize=12)
    axes[0].set_ylabel("Number of Sales", fontsize=12)
    axes[0].legend(title="Category", fontsize=10)
    axes[0].grid(axis="y", linestyle="--", alpha=0.6)

    # === Plot 2: Profit Per Location (Heatmap without Seaborn) ===
    locations = location_profit["Location"].values
    profits = location_profit["Profit"].values.reshape(-1, 1)  # Reshape for heatmap

    heatmap = axes[1].imshow(profits, cmap=plt.cm.RdYlGn, aspect="auto")

    # Display values inside heatmap cells
    for i, profit in enumerate(profits):
        axes[1].text(0, i, f"{int(profit[0])}", ha="center", va="center", fontsize=12, fontweight="bold", color="black")

    axes[1].set_xticks([])  # Remove x-axis ticks
    axes[1].set_yticks(range(len(locations)))
    axes[1].set_yticklabels(locations, fontsize=12)

    axes[1].set_title("Profit Per Location (Heatmap)", fontsize=14, fontweight="bold")
    axes[1].set_ylabel("Location", fontsize=12)

    # Add color bar
    cbar = plt.colorbar(heatmap, ax=axes[1], fraction=0.046, pad=0.04)
    cbar.set_label("Profit", fontsize=12)

    plt.tight_layout()
    return fig

# === Example Usage ===
if __name__ == "__main__":
    # Load Test Data from 'tests' Folder
    sales_df = pd.read_csv("tests/s3.csv")
    products_df = pd.read_csv("tests/p3.csv")

    # Generate the figure
    fig = analyze_category_and_profit(sales_df, products_df)

    # Show the figure
    plt.show()
