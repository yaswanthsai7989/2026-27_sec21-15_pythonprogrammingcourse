a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a >0 and b > 0 and c > 0:
    if a+b+c==180:
        print("The angles form a valid triangle.")
    else:
        print("The angles do not form a valid triangle.")
else:
    print("Please enter positive numbers only.")
    