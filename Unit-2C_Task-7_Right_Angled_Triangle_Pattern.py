#Write a python program to print a right-angled triangle pattern; read the number of rows and the symbol to print (e.g. * or 0) from the user
rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")

for i in range(rows):
    for j in range(i + 1):
        print(symbol, end=' ')
    print()  # Move to the next line after each row