#Write a python program to demonstrate string formatting (format(), f-strings, % operator)

name = "Ravi"
age = 18
marks = 95

# 1. Using format()
print("My name is {}. I am {} years old.".format(name, age))

# 2. Using f-strings
print(f"My name is {name}. I am {age} years old.")

# 3. Using % operator
print("My name is %s. I am %d years old." % (name, age))

# Display marks using all three methods
print("Marks = {}".format(marks))
print(f"Marks = {marks}")
print("Marks = %d" % marks)
