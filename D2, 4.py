def is_prime(n: int) -> bool:
    # Check if n is less than 2, since prime numbers are greater than 1
    if n <= 1:
        return False
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # Should return True because 7 is a prime number
print(is_prime(8))  # Should return False because 8 is not a prime number (it's divisible by 2 and 4)