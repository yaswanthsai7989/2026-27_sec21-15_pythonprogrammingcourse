# Create a list
numbers = [1, 2, 3, 4, 5, 6]

# Find squares using list comprehension
squares = [n*n for n in numbers]
print("Squares:", squares)

# Filter even numbers using list comprehension
even = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even)