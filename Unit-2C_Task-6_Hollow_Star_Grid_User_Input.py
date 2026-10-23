#Write a python program to print a 5x5 hollow grid of stars (*); generalize the program so the grid size is based on user input
size = int(input("Enter the size of the grid: "))
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()  # Move to the next line after each row