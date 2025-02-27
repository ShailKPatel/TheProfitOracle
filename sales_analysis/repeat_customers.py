import pandas as pd
import matplotlib.pyplot as plt

def analyze_repeat_customers(sales_df):
    """
    Analyzes repeat customers within different time windows.

    Parameters:
    - sales_df (pd.DataFrame): Contains 'CID', 'Date', and 'Location'.

    Returns:
    - repeat_customer_df (pd.DataFrame): Number of repeat customers in 7 days, 4 weeks, and 3 months.
    - fig (matplotlib.figure.Figure): Bar chart of average repeat duration per location.
    """

    # Ensure 'Date' is in datetime format
    sales_df["Date"] = pd.to_datetime(sales_df["Date"], errors="coerce")

    # Define time windows
    end_date = sales_df["Date"].max()
    time_windows = {
        "Last 7 Days": end_date - pd.Timedelta(days=7),
        "Last 4 Weeks": end_date - pd.Timedelta(weeks=4),
        "Last 3 Months": end_date - pd.Timedelta(days=90),
    }

    # Count repeat customers in each window
    repeat_counts = {}
    for period, start_date in time_windows.items():
        recent_sales = sales_df[sales_df["Date"] >= start_date]
        repeat_customers = recent_sales.groupby("CID").filter(lambda x: len(x) > 1)["CID"].nunique()
        repeat_counts[period] = repeat_customers

    # Create a DataFrame for repeat customer counts
    repeat_customer_df = pd.DataFrame(
        list(repeat_counts.items()), columns=["Time Period", "Repeat Customers"]
    )

    # Calculate average repeat duration per location
    sales_df["Days_Since_Last_Purchase"] = sales_df.groupby("CID")["Date"].diff().dt.days
    avg_repeat_per_location = sales_df.groupby("Location")["Days_Since_Last_Purchase"].mean().dropna()

    # Plot bar chart of average repeat duration per location
    fig, ax = plt.subplots(figsize=(8, 5))
    avg_repeat_per_location.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")

    ax.set_xlabel("Location")
    ax.set_ylabel("Avg Days Between Repeat Purchases")
    ax.set_title("Average Repeat Purchase Duration per Location")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    return repeat_customer_df, fig


# === Example Usage ===
if __name__ == "__main__":
    # Load test data
    sales_df = pd.read_csv("tests/s3.csv")

    # Run analysis
    repeat_df, fig = analyze_repeat_customers(sales_df)

    # Display results
    print(repeat_df)
    plt.show()
