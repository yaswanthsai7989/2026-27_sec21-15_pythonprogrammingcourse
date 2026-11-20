# Create a class
class Student:

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Create a method
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

# Create an object
s1 = Student("Yaswanth", 101)

# Access attributes and method
s1.display()