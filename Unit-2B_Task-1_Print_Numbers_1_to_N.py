#Write a python program to print numbers from 1 to N
1. using for loop
2. using while loop

# Using for loop
N = int(input("Enter the value of N: "))
for i in range(1, N + 1):
    print(i, end=" ")

# Using while loop
N = int(input("Enter the value of N: "))
i = 1
while i <= N:
    print(i, end=" ")
    i += 1              