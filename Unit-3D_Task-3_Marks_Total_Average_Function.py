def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Input marks
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

# Function call
total, average = calculate_marks(m1, m2, m3)

# Display result
print("Total Marks:", total)
print("Average Marks:", round(average, 2))