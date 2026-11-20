# Create a list of dictionaries
students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Yaswanth", "marks": 95},
    {"name": "Anil", "marks": 75}
]

# Sort based on marks
students.sort(key=lambda x: x["marks"])

# Display sorted list
print("Students Sorted by Marks:")
for student in students:
    print(student)
    