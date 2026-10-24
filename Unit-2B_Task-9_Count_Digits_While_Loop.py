#Write a python program to count the number of digits in a number using while loop
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)