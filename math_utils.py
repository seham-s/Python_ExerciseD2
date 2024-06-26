# math_utils.py

# Function to return the sum of two numbers
def add(x, y):
    return x + y

# Function to return the difference between two numbers
def subtract(x, y):
    return x - y

# Function to return the product of two numbers
def multiply(x, y):
    return x * y

# Function to return the division of two numbers
def divide(x, y):
    # Check for division by zero and return None if y is 0
    if y == 0:
        return None
    return x / y