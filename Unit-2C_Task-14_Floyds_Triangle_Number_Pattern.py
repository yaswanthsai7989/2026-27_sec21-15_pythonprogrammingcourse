#Write a python program to print a number pattern (e.g., Floyd's triangle)
rows = int(input("Enter the number of rows: "))
num = 1
for i in range(rows):
    for j in range(i + 1):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line after each row 