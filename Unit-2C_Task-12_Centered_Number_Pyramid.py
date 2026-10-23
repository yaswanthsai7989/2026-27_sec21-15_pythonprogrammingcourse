#Write a python program to print a centered number pyramid
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    # Print spaces for centering
    for j in range(rows - i - 1):
        print(" ", end=' ')
    # Print numbers
    for k in range(2 * i + 1):
        print(k + 1, end=' ')
    print()  # Move to the next line after each row