class Student:
    def __init__(self):
        self._name = "Yaswanth"       # Protected attribute
        self.__marks = 90             # Private attribute

    def display(self):
        print("Name:", self._name)
        print("Marks:", self.__marks)

# Create object
s1 = Student()

# Access attributes
print("Protected:", s1._name)
s1.display()