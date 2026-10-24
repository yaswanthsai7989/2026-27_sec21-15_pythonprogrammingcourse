#Write a python program to check whether a number is an Armstrong number using while loop
(assume the number has 3 digits)
num = int(input("Enter a 3-digit number: "))
original_num = num
sum_of_cubes = 0
while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num //= 10
if sum_of_cubes == original_num:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")