#Write a python program to print the grade of a student using an elif ladder (Marks >= 90 → Grade A; >= 80 and < 90 → Grade B; >= 70 and < 80 → Grade C; < 70 → Grade D)
marks = float(input("Enter the marks of the student: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")