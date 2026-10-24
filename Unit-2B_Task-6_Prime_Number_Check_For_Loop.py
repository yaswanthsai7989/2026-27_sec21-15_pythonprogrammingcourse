#Write a python program to check whether a given number is prime or not using for loop
(assume the input number is between 1 and 100)
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")