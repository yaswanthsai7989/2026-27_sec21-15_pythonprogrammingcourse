#Write a python program to print numbers in a 3x3 grid (as shown in the hint) using for-for nested loop	
for i in range(3):
    for j in range(3):
        print(i * 3 + j + 1, end=' ')
    print()  # Move to the next line after each row