#Write a python program to check whether a string is a palindrome
string = input("Enter a string: ")
# Remove spaces and convert to lowercase for uniformity
cleaned_string = string.replace(" ", "").lower()
# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")