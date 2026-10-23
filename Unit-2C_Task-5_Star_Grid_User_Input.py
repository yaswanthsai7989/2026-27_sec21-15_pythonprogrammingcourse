#Write a python program to print a 5x5 grid of stars (*); generalize the program so the grid size is based on user input
size = int(input("Enter the size of the grid: "))
for i in range(size):
    for j in range(size):
        print("*", end=' ')
    print()  # Move to the next line after each row