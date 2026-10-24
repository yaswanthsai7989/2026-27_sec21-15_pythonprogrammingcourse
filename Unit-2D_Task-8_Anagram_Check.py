#Write a python program to check whether two strings are anagrams
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Convert strings to lowercase and remove spaces
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
# Check if the sorted characters of both strings are equal
if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")