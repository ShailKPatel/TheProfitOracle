import matplotlib.pyplot as plt
import pandas as pd

def plot_sales_trends(sales_df):    
    """
    Analyzes and visualizes sales trends over time.

    This function takes a DataFrame containing sales data and generates
    three time-series plots:
    1. Daily Sales with a 7-day moving average
    2. Weekly Sales with a 4-week moving average
    3. Monthly Sales with a 3-month moving average

    Parameters:
        sales_df (pd.DataFrame): DataFrame containing 'Date' and 'Sales_Price' columns.

    Returns:
        matplotlib.figure.Figure: A figure containing the three sales trend plots.
    """

    # Ensure 'Date' column is in datetime format (to avoid incorrect sorting and calculations)
    sales_df["Date"] = pd.to_datetime(sales_df["Date"], errors="coerce")

    # Remove rows where 'Date' conversion failed (i.e., null values)
    sales_df = sales_df.dropna(subset=["Date"])

    # === Resampling and Grouping Data ===
    # Resampling means aggregating data at different time intervals.

    # Group sales by **each day**, summing up the sales price
    daily_sales = sales_df.groupby("Date")["Sales_Price"].sum()

    # Group sales by **week**, summing sales for each week
    weekly_sales = sales_df.resample("W", on="Date")["Sales_Price"].sum()

    # Group sales by **month**, summing sales for each month
    monthly_sales = sales_df.resample("M", on="Date")["Sales_Price"].sum()

    # === Moving Averages (MA) ===
    # A moving average smooths out short-term fluctuations and highlights trends over time.
    # It is calculated by taking the mean of a fixed number of previous data points.

    # 7-day moving average for daily sales (smoother trends)
    daily_sales_ma = daily_sales.rolling(window=7).mean()

    # 4-week moving average for weekly sales
    weekly_sales_ma = weekly_sales.rolling(window=4).mean()

    # 3-month moving average for monthly sales
    monthly_sales_ma = monthly_sales.rolling(window=3).mean()

    # === Plotting ===
    # Create a figure with 3 vertically stacked subplots
    fig, axes = plt.subplots(3, 1, figsize=(12, 14))

    # Define a color scheme for better visualization
    colors = {"sales": "#1f77b4", "ma": "#d62728"}  # Blue for sales, Red for moving avg

    # --- Daily Sales Plot ---
    axes[0].plot(daily_sales.index, daily_sales, label="Daily Sales", color=colors["sales"], alpha=0.7)
    axes[0].plot(daily_sales_ma.index, daily_sales_ma, label="7-Day Moving Avg", color=colors["ma"], linestyle="--", linewidth=2)
    axes[0].set_title("Daily Sales Trend", fontsize=14, fontweight="bold")
    axes[0].set_ylabel("Total Sales", fontsize=12)
    axes[0].legend()
    axes[0].grid(True, linestyle="--", alpha=0.6)

    # --- Weekly Sales Plot ---
    axes[1].plot(weekly_sales.index, weekly_sales, label="Weekly Sales", color=colors["sales"], alpha=0.7)
    axes[1].plot(weekly_sales_ma.index, weekly_sales_ma, label="4-Week Moving Avg", color=colors["ma"], linestyle="--", linewidth=2)
    axes[1].set_title("Weekly Sales Trend", fontsize=14, fontweight="bold")
    axes[1].set_ylabel("Total Sales", fontsize=12)
    axes[1].legend()
    axes[1].grid(True, linestyle="--", alpha=0.6)

    # --- Monthly Sales Plot ---
    axes[2].plot(monthly_sales.index, monthly_sales, label="Monthly Sales", color=colors["sales"], alpha=0.7)
    axes[2].plot(monthly_sales_ma.index, monthly_sales_ma, label="3-Month Moving Avg", color=colors["ma"], linestyle="--", linewidth=2)
    axes[2].set_title("Monthly Sales Trend", fontsize=14, fontweight="bold")
    axes[2].set_ylabel("Total Sales", fontsize=12)
    axes[2].legend()
    axes[2].grid(True, linestyle="--", alpha=0.6)


    # Adjust layout and show plots
    plt.tight_layout()
    return plt

# Example usage
if __name__ == "__main__":
    # Load sales data
    sales_df = pd.read_csv("tests/s3.csv")

    # Ensure the necessary columns exist before plotting
    required_columns = {"Date", "Sales_Price"}
    if required_columns.issubset(sales_df.columns):
        fig = plot_sales_trends(sales_df)
        fig.show()  # Display the generated figure
    else:
        print("Error: Sales data must contain 'Date' and 'Sales_Price' columns.")