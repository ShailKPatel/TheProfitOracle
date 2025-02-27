import pandas as pd
import os

# Define allowed file extensions
VALID_EXTENSIONS = ('.csv', '.xls', '.xlsx', '.xlsm', '.xlsb')

# Custom exceptions
class InvalidFileExtensionError(Exception):
    """Raised when the file provided is not of a supported format."""
    pass

class CorruptedFileError(Exception):
    """Raised when the file cannot be converted to a DataFrame."""
    pass

class DuplicateKeyError(Exception):
    """Raised when a duplicate key is found in a unique column."""
    pass

def check_extension(file_path):
    """
    Checks if the file extension is valid.
    
    Parameters:
        file_path (str): Path of the file to check.

    Raises:
        InvalidFileExtensionError: If the file extension is not in VALID_EXTENSIONS.
    """
    _, file_extension = os.path.splitext(file_path)  # Extract file extension
    if file_extension.lower() not in VALID_EXTENSIONS:
        raise InvalidFileExtensionError(f"Unsupported file format: {file_extension}")

def convert_to_df(file_path):
    """
    Attempts to read a file and convert it into a Pandas DataFrame.

    Parameters:
        file_path (str): Path to the file.

    Returns:
        pd.DataFrame: The loaded DataFrame.

    Raises:
        CorruptedFileError: If the file cannot be read as a DataFrame.
    """
    try:
        if file_path.lower().endswith(".csv"):
            return pd.read_csv(file_path)  # Read CSV file
        else:
            return pd.read_excel(file_path)  # Read Excel file
    except Exception as e:
        raise CorruptedFileError(f"Failed to load file: {file_path}") from e

def check_unique_column(df, column_name):
    """
    Checks for duplicate values in a specific column.

    Parameters:
        df (pd.DataFrame): DataFrame to check.
        column_name (str): The column that must contain unique values.

    Raises:
        DuplicateKeyError: If duplicate values are found.
    """
    if df.duplicated(subset=[column_name]).any():
        raise DuplicateKeyError(f"Duplicate values found in column: {column_name}")

def remove_empty(df):
    """
    Removes any row that contains NaN values.

    Parameters:
        df (pd.DataFrame): DataFrame to clean.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    return df.dropna(axis=0)  # Drop rows where any value is NaN

def process_product_file(file_path):
    """
    Processes the product file:
    1. Checks file extension.
    2. Converts to DataFrame.
    3. Ensures unique 'PID' values.
    4. Removes columns with NaN values.

    Parameters:
        file_path (str): Path to the product file.

    Returns:
        pd.DataFrame: Cleaned Product DataFrame.
    """
    check_extension(file_path)  # Validate file type
    df = convert_to_df(file_path)  # Convert to DataFrame

    df = remove_empty(df)  # Remove empty columns
    check_unique_column(df, "PID")  # Ensure 'PID' is unique

    return df  # Return cleaned DataFrame

def process_sales_file(file_path):
    """
    Processes the sales file:
    1. Checks file extension.
    2. Converts to DataFrame.
    3. Replaces NaN in 'CID' with '0'.
    4. Ensures unique 'SID' values.
    5. Removes columns with NaN values.

    Parameters:
        file_path (str): Path to the sales file.

    Returns:
        pd.DataFrame: Cleaned Sales DataFrame.
    """
    check_extension(file_path)
    df = convert_to_df(file_path)

    # Replace NaN values in 'CID' with "0"
    if "CID" in df.columns:
        df["CID"] = df["CID"].fillna("0")

    df = remove_empty(df)  # Remove empty columns
    check_unique_column(df, "SID")  # Ensure 'SID' is unique

    return df

def process_customer_file(file_path):
    """
    Processes the customer file:
    1. Checks file extension.
    2. Converts to DataFrame.
    3. Ensures unique 'CID' values.
    4. Removes invalid 'Age' and 'Gender' rows.
    5. Removes columns with NaN values.

    Parameters:
        file_path (str): Path to the customer file.

    Returns:
        pd.DataFrame: Cleaned Customer DataFrame.
    """
    check_extension(file_path)
    df = convert_to_df(file_path)


    # Validate Age column
    if "Age" in df.columns:
        df = df[(df["Age"] >= 0) & (df["Age"] <= 120)]  # Keep valid ages

    # Validate Gender column
    if "Gender" in df.columns:
        valid_genders = {"Male", "Female", "Trans"}
        df = df[df["Gender"].isin(valid_genders)]  # Keep valid genders

    df = remove_empty(df)  # Remove empty columns
    check_unique_column(df, "CID")  # Ensure 'CID' is unique

    return df


if __name__ == "__main__":
    # Example usage of the functions
    product_df = process_product_file("tests/p3.csv")
    sales_df = process_sales_file("tests/s2.csv")
    customer_df = process_customer_file("tests/c2.csv")

    # Display loaded DataFrames
    print("Product Data:\n", product_df)
    print("\nSales Data:\n", sales_df)
    print("\nCustomer Data:\n", customer_df)
