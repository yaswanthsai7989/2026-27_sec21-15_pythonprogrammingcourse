#Write a python program to print numbers in a 3x3 grid (as shown in the hint) using while-for nested loop
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(i * 3 + j + 1, end=' ')
        j += 1
    print()
    i += 1