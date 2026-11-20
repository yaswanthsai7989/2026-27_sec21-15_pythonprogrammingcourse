# Create a class
class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Display details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create object
s1 = Student("Yaswanth", 18)

# Call method
s1.display()