# factorial.py

from typing import List

# Function to compute the factorial of a number
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)