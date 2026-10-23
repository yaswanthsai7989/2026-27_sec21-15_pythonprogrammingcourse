#Write a python program to print a centered pyramid pattern of stars
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    # Print spaces for centering
    for j in range(rows - i - 1):
        print(" ", end=' ')
    # Print stars
    for k in range(2 * i + 1):
        print("*", end=' ')
    print()  # Move to the next line after each row