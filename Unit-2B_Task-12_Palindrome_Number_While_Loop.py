#Write a python program to check whether a number is a palindrome using while loop
num = int(input("Enter a number: "))
original_num = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if reverse == original_num:
    print(original_num, "is a palindrome.")
else:
    print(original_num, "is not a palindrome.")