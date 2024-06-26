# prime_numbers.py

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    count = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            count += 1
    return count

# Prompt the user to enter a number
number = int(input("Enter a number to find all primes up to that number: "))

# Count the number of prime numbers up to the entered number
prime_count = count_primes(number)

# Print the result
print(f"There are {prime_count} prime numbers up to {number}.")