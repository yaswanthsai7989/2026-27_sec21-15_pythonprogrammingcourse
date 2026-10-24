#Write a python program to find the largest number in a series of N numbers entered by the user using for loop
N = int(input("Enter the value of N: "))
largest = float('-inf')  # Initialize largest to the smallest possible value
for i in range(N):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
print("The largest number is:", largest)