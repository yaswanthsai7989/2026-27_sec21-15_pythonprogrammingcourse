# Create a dictionary
student = {
    "name": "Yaswanth",
    "roll_no": 101,
    "branch": "CSE"
}

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display items
print("Items:", student.items())

# Access value using get()
print("Name:", student.get("name"))

# Update dictionary
student.update({"branch": "Cyber Security"})
print("After Update:", student)

# Remove an item using pop()
student.pop("roll_no")
print("After Pop:", student)