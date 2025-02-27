import numpy as np

class DataLengthMismatchError(Exception):
    """Custom exception for mismatched input lengths."""
    pass

def validate_data(x, y):
    """
    Validates the input data:
    - Checks if x and y have the same length.
    - Checks if all elements are numeric.
    - Converts them to float if necessary.
    """
    if len(x) != len(y):
        raise DataLengthMismatchError("Input columns must have the same length.")

    # Convert to NumPy array and check for NaN values
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    if np.isnan(x).any() or np.isnan(y).any():
        raise ValueError("Input contains NaN values. Please clean the data.")

    return x, y

def compute_cost(x, y, w, b):
    """
    Computes the Mean Squared Error (MSE) cost function.
    """
    n = len(y)
    y_pred = w * x + b  # Predicted values
    cost = (1 / (2 * n)) * np.sum((y_pred - y) ** 2)
    return cost

def gradient_descent(x, y, w, b, learning_rate, epochs):
    """
    Optimizes w (weight) and b (bias) using gradient descent.
    """
    n = len(y)
    for _ in range(epochs):
        # Compute predictions
        y_pred = w * x + b
        
        # Compute gradients
        dw = (1 / n) * np.sum((y_pred - y) * x)
        db = (1 / n) * np.sum(y_pred - y)
        
        # Update parameters
        w -= learning_rate * dw
        b -= learning_rate * db
    
    return w, b

def linear_regression(x, y, learning_rate=0.01, epochs=1000):
    """
    Performs simple linear regression using gradient descent.
    Returns optimized values of w (weight) and b (bias).
    """
    x, y = validate_data(x, y)  # Ensure x and y are clean numeric arrays
    
    w, b = 0.0, 0.0  # Initialize parameters
    w, b = gradient_descent(x, y, w, b, learning_rate, epochs)
    
    return w, b

# === Example Usage ===
if __name__ == "__main__":
    # Sample Data
    x = np.array([1, 2, 3, 4, 5])  # Independent variable
    y = np.array([2, 4, 6, 8, 10])  # Dependent variable
    
    # Train model
    w, b = linear_regression(x, y)
    
    print(f"Optimized weight (w): {w:.4f}")
    print(f"Optimized bias (b): {b:.4f}")
