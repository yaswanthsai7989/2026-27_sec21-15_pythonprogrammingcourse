#Write a python program to find the sum and average of N numbers using for loop
N = int(input("Enter the value of N: "))
sum = 0
for i in range(1, N + 1):
    sum += i
average = sum / N if N > 0 else 0
print("Sum:", sum)
print("Average:", average)