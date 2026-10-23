#Write a python program to print an inverted right-angled triangle pattern
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(rows - i):
        print("*", end=' ')
    print()  # Move to the next line after each row 