import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_sales_by_location(sales_df, customers_df):
    """
    Analyzes sales performance across locations by considering:
    1. Total Sales per Location
    2. Total Unique Customers per Location
    3. Gender Distribution & Median Age per Location

    Parameters:
    - sales_df (pd.DataFrame): DataFrame containing 'Location', 'CID', and 'Sales_Price' columns.
    - customers_df (pd.DataFrame): DataFrame containing 'CID', 'Age', and 'Gender' columns.

    Returns:
    - matplotlib.figure.Figure: A figure containing three analysis plots.
    """

    # === Step 1: Merge Sales Data with Customer Data ===
    sales_with_customers = sales_df.merge(customers_df, on="CID", how="left")

    # === Step 2: Aggregate Sales by Location ===
    location_sales = sales_with_customers.groupby("Location")["Sales_Price"].sum().sort_values(ascending=False)

    # === Step 3: Count Unique Customers Per Location ===
    unique_customers_per_location = sales_with_customers.groupby("Location")["CID"].nunique()

    # === Step 4: Gender & Age Analysis Per Location ===
    gender_counts = sales_with_customers.pivot_table(index="Location", columns="Gender", values="CID", aggfunc="count", fill_value=0)
    median_age = sales_with_customers.groupby("Location")["Age"].median()

    # === Step 5: Plotting ===
    fig, axes = plt.subplots(3, 1, figsize=(48, 72))
    plt.subplots_adjust(hspace=0.5)  # Better spacing between subplots

    # === Plot 1: Total Sales Per Location ===
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33A8"]
    bars = axes[0].bar(location_sales.index, location_sales.values, color=colors[:len(location_sales)], label="Total Sales")

    axes[0].set_title("Total Sales per Location", fontsize=14, fontweight="bold", color="black")
    axes[0].set_xlabel("Location", fontsize=12)
    axes[0].set_ylabel("Total Sales", fontsize=12)
    axes[0].grid(axis="y", linestyle="--", alpha=0.6)

    # Adding Value Labels on Bars
    for bar in bars:
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{bar.get_height():,.0f}",
                        ha="center", va="bottom", fontsize=10, fontweight="bold")

    axes[0].legend()

    # === Plot 2: Total Unique Customers Per Location ===
    bars = axes[1].bar(unique_customers_per_location.index, unique_customers_per_location.values, color="#1f77b4", label="Unique Customers")

    axes[1].set_title("Total Unique Customers per Location", fontsize=14, fontweight="bold", color="black")
    axes[1].set_xlabel("Location", fontsize=12)
    axes[1].set_ylabel("Number of Unique Customers", fontsize=12)
    axes[1].grid(axis="y", linestyle="--", alpha=0.6)

    # Adding Value Labels on Bars
    for bar in bars:
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{int(bar.get_height())}",
                        ha="center", va="bottom", fontsize=10, fontweight="bold")

    axes[1].legend()

    # === Plot 3: Gender Distribution & Median Age Per Location ===
    width = 0.6  # Bar width for stacking
    gender_colors = {"Male": "#3366CC", "Female": "#FF66B2"}  # Blue for Male, Pink for Female
    gender_bars = gender_counts.plot(kind="bar", stacked=True, color=[gender_colors.get(g, "#999999") for g in gender_counts.columns], ax=axes[2])

    # Overlay median age on top of gender bars
    for i, loc in enumerate(median_age.index):
        total_height = gender_counts.loc[loc].sum()
        axes[2].text(i, total_height + 1, f"Age: {int(median_age[loc])}", ha="center", fontsize=10, fontweight="bold", color="black")

    axes[2].set_title("Gender Distribution & Median Age per Location", fontsize=14, fontweight="bold", color="black")
    axes[2].set_xlabel("Location", fontsize=12)
    axes[2].set_ylabel("Customer Count", fontsize=12)
    axes[2].grid(axis="y", linestyle="--", alpha=0.6)

    # Adding a legend
    axes[2].legend(title="Gender")

    plt.tight_layout()
    return fig

# === Example Usage ===
if __name__ == "__main__":
    # Sample Data (Replace this with actual DataFrames)
    sales_data = {
        "Date": pd.date_range(start="2024-01-01", periods=30, freq="D").tolist() * 3,
        "Sales_Price": np.random.randint(100, 1000, 90),
        "Location": ["A"] * 30 + ["B"] * 30 + ["C"] * 30,
        "CID": np.random.randint(1, 20, 90)  # Random customer IDs
    }
    sales_df = pd.DataFrame(sales_data)
    sales_df["Date"] = pd.to_datetime(sales_df["Date"])

    customer_data = {
        "CID": list(range(1, 20)),
        "Age": np.random.randint(18, 60, 19),
        "Gender": np.random.choice(["Male", "Female"], 19)
    }
    customers_df = pd.DataFrame(customer_data)

    # Generate the figure
    fig = analyze_sales_by_location(sales_df, customers_df)

    # Show the figure
    plt.show()
