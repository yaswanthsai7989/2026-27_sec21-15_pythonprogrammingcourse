#Write a python program to print Pascal's triangle
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    # Print leading spaces for centering
    for j in range(rows - i - 1):
        print(" ", end=' ')
    
    # Calculate and print the values in Pascal's triangle
    value = 1
    for k in range(i + 1):
        print(value, end=' ')
        value = value * (i - k) // (k + 1)  # Update the value for the next position
    
    print()  # Move to the next line after each row