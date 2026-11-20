# Create a dictionary using dictionary comprehension
squares = {n: n*n for n in range(1, 6)}

print("Squares Dictionary:", squares)

# Create a dictionary of even numbers
even = {n: n*n for n in range(1, 11) if n % 2 == 0}

print("Even Squares:", even)