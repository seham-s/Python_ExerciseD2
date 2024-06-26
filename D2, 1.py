def calculate(int1: int, int2: int):
    # Calculate the sum of the two integers
    sum_result = int1 + int2
    # Calculate the difference of the two integers (int1 - int2)
    difference_result = int1 - int2
    # Calculate the product of the two integers
    product_result = int1 * int2

    # Print the results
    print(f"The sum of {int1} and {int2} is: {sum_result}")
    print(f"The difference between {int1} and {int2} is: {difference_result}")
    print(f"The product of {int1} and {int2} is: {product_result}")

# Call the function with the integers 3 and 9
calculate(3, 9)