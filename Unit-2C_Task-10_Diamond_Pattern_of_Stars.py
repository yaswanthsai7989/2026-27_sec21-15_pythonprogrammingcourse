#Write a python program to print a diamond pattern of stars
rows = int(input("Enter the number of rows: "))
# Upper part of the diamond
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=' ')
    for k in range(2 * i + 1):
        print("*", end=' ')
    print()
# Lower part of the diamond
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end=' ')
    for k in range(2 * i + 1):
        print("*", end=' ')
    print()