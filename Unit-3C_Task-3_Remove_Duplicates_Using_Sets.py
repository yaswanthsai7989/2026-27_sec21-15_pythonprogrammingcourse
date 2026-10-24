#Write a python program to remove duplicates from a list using sets
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("Original list:", my_list)
print("List after removing duplicates:", unique_list)