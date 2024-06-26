# factorial.py

from typing import List

# Function to compute the factorial of a number
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Function to compute a list of factorials from a list of numbers
def list_factorial(lst: List[int]) -> List[int]:
    return [factorial(number) for number in lst]