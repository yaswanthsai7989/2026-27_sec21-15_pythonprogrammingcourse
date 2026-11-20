class Student:
    def __init__(self):
        self.__marks = 0

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks

# Create object
s1 = Student()

# Set and get marks
s1.set_marks(90)

print("Student Marks:", s1.get_marks())