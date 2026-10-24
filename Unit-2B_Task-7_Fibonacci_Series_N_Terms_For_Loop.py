#Write a python program to print Fibonacci series up to N terms using for loop
N = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b