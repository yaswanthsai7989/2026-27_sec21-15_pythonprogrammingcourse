# Create a nested dictionary
students = {
    1: {
        "name": "Yaswanth",
        "branch": "CSE",
        "marks": 90
    },
    2: {
        "name": "Rahul",
        "branch": "ECE",
        "marks": 85
    }
}

# Access dictionary elements
print("Student 1 Details:")
print("Name:", students[1]["name"])
print("Branch:", students[1]["branch"])
print("Marks:", students[1]["marks"])

print("\nStudent 2 Details:")
print("Name:", students[2]["name"])
print("Branch:", students[2]["branch"])
print("Marks:", students[2]["marks"])