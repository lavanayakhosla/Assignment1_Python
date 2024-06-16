def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = 10

# Generate the first n Fibonacci numbers
fib_numbers = generate_fibonacci(n)

# Print the result
print(f"The first {n} Fibonacci numbers are:", fib_numbers)
