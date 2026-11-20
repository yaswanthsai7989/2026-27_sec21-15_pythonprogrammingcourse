
# File: mypackage/__init__.py
# Custom package


# File: mypackage/addition.py
def add(a, b):
    return a + b


# File: mypackage/subtraction.py
def subtract(a, b):
    return a - b


# File: main.py
from mypackage import addition, subtraction

print("Addition:", addition.add(10, 5))
print("Subtraction:", subtraction.subtract(10, 5))
