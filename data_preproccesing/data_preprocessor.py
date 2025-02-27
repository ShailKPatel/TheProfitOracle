import pandas as pd

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

def check_extension(file):
    """
    Checks if the uploaded file has a valid extension.

    Parameters:
        file (UploadedFile): Streamlit file uploader object.

    Raises:
        InvalidFileExtensionError: If the file extension is not in VALID_EXTENSIONS.
    """
    if file is None:
        raise InvalidFileExtensionError("No file uploaded. Please select a file.")

    if not file.name.endswith(VALID_EXTENSIONS):  # Validate file extension from .name attribute
        raise InvalidFileExtensionError(f"Invalid file format: {file.name}. Allowed formats: {VALID_EXTENSIONS}")

def convert_to_df(file):
    """
    Reads an uploaded file into a Pandas DataFrame.

    Parameters:
        file (UploadedFile): The uploaded file object.

    Returns:
        pd.DataFrame: The loaded DataFrame.

    Raises:
        CorruptedFileError: If the file cannot be read as a DataFrame.
    """
    try:
        if file.name.endswith(".csv"):
            return pd.read_csv(file)  # Read CSV file from file object
        else:
            return pd.read_excel(file)  # Read Excel file from file object
    except Exception as e:
        raise CorruptedFileError(f"Failed to load file: {file.name}") from e

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

def process_product_file(file):
    """
    Processes the product file:
    1. Checks file extension.
    2. Converts to DataFrame.
    3. Ensures unique 'PID' values.
    4. Removes columns with NaN values.

    Parameters:
        file (UploadedFile): The uploaded product file.

    Returns:
        pd.DataFrame: Cleaned Product DataFrame.
    """
    check_extension(file)  # Validate file type
    df = convert_to_df(file)  # Convert to DataFrame

    df = remove_empty(df)  # Remove empty columns
    check_unique_column(df, "PID")  # Ensure 'PID' is unique

    return df  # Return cleaned DataFrame

def process_sales_file(file):
    """
    Processes the sales file:
    1. Checks file extension.
    2. Converts to DataFrame.
    3. Replaces NaN in 'CID' with '0'.
    4. Ensures unique 'SID' values.
    5. Removes columns with NaN values.

    Parameters:
        file (UploadedFile): The uploaded sales file.

    Returns:
        pd.DataFrame: Cleaned Sales DataFrame.
    """
    check_extension(file)
    df = convert_to_df(file)

    # Replace NaN values in 'CID' with "0"
    if "CID" in df.columns:
        df["CID"] = df["CID"].fillna("0")

    df = remove_empty(df)  # Remove empty columns
    check_unique_column(df, "SID")  # Ensure 'SID' is unique

    return df

def process_customer_file(file):
    """
    Processes the customer file:
    1. Checks file extension.
    2. Converts to DataFrame.
    3. Ensures unique 'CID' values.
    4. Removes invalid 'Age' and 'Gender' rows.
    5. Removes columns with NaN values.

    Parameters:
        file (UploadedFile): The uploaded customer file.

    Returns:
        pd.DataFrame: Cleaned Customer DataFrame.
    """
    check_extension(file)
    df = convert_to_df(file)

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
    # Example usage of the functions with file objects
    with open("tests/p3.csv", "rb") as product_file, \
            open("tests/s3.csv", "rb") as sales_file, \
            open("tests/c3.csv", "rb") as customer_file:

        product_df = process_product_file(product_file)
        sales_df = process_sales_file(sales_file)
        customer_df = process_customer_file(customer_file)

    # Display loaded DataFrames
    print("Product Data:\n", product_df)
    print("\nSales Data:\n", sales_df)
    print("\nCustomer Data:\n", customer_df)

