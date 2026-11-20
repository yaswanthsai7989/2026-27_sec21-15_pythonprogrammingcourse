class Student:
    college = "ABC College"

    # Instance method
    def display(self):
        print("Name:", self.name)

    # Class method
    @classmethod
    def college_name(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def message():
        print("Welcome to Python")

# Create object
s1 = Student()
s1.name = "Yaswanth"

# Call methods
s1.display()
Student.college_name()
Student.message()