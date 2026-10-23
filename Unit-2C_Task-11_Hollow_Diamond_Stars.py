#Write a python program to print a hollow diamond pattern of stars
rows = int(input("Enter the number of rows: "))
# Upper part of the diamond
for i in range(rows):   
    for j in range(rows - i - 1):
        print(" ", end=' ')
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()