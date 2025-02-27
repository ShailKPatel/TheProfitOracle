import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_profit_per_category(sales_df, products_df):
    """
    Analyzes average manufacturing cost and sales price per product category.

    Parameters:
    - sales_df (pd.DataFrame): Contains 'PID', 'Sales_Price'.
    - products_df (pd.DataFrame): Contains 'PID', 'Manufacturing Cost', 'Category'.

    Returns:
    - fig (matplotlib.figure.Figure): A bar chart comparing average manufacturing cost and sales price per category.
    """

    # Merge sales data with product details
    merged_df = sales_df.merge(products_df, on="PID", how="left")

    # Calculate average values per category
    category_stats = merged_df.groupby("Category").agg(
        Avg_Manufacturing_Cost=("Manufacturing Cost", "mean"),
        Avg_Sales_Price=("Sales_Price", "mean")
    )

    # Define bar positions with spacing between categories
    categories = category_stats.index
    num_categories = len(categories)
    indices = np.arange(num_categories) * 2.5  # Adds spacing between category pairs

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar width
    bar_width = 0.8

    # Plot manufacturing cost (Red)
    ax.bar(indices - bar_width / 2, category_stats["Avg_Manufacturing_Cost"], 
            width=bar_width, color="red", edgecolor="black", label="Avg Manufacturing Cost")

    # Plot selling price (Green)
    ax.bar(indices + bar_width / 2, category_stats["Avg_Sales_Price"], 
            width=bar_width, color="green", edgecolor="black", label="Avg Sales Price")

    # Annotate values on bars
    for i, category in enumerate(categories):
        avg_manufacturing = category_stats.loc[category, "Avg_Manufacturing_Cost"]
        avg_selling = category_stats.loc[category, "Avg_Sales_Price"]

        ax.text(indices[i] - bar_width / 2, avg_manufacturing + 0.5, f"{avg_manufacturing:.2f}",
                ha="center", va="bottom", color="black", fontsize=10)
        ax.text(indices[i] + bar_width / 2, avg_selling + 0.5, f"{avg_selling:.2f}",
                ha="center", va="bottom", color="black", fontsize=10)

    # Labels and title
    ax.set_xlabel("Category")
    ax.set_ylabel("Price (in Currency)")
    ax.set_title("Average Manufacturing Cost vs Sales Price per Category")
    ax.set_xticks(indices)
    ax.set_xticklabels(categories, rotation=45, ha="right")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    return fig


# === Example Usage ===
if __name__ == "__main__":
    # Load test data
    sales_df = pd.read_csv("tests/s3.csv")
    products_df = pd.read_csv("tests/p3.csv")

    # Run analysis
    fig = analyze_profit_per_category(sales_df, products_df)

    # Display results
    plt.show()
