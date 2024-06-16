def sum_of_digits(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())

# Example usage:
number = 12345

# Calculate the sum of digits of the number
digit_sum = sum_of_digits(number)

# Print the result
print(f"The sum of digits of {number} is:", digit_sum)
