#Write a python program to demonstrate set membership testing and methods (add, remove, discard)
my_set = {1, 2, 3, 4, 5}
# Membership testing
print(3 in my_set)  # True
print(6 in my_set)  # False
# Adding an element
my_set.add(6)
print("Set after adding 6:", my_set)
# Removing an element
my_set.remove(3)
print("Set after removing 3:", my_set)
# Discarding an element (won't raise an error if the element is not found)
my_set.discard(10)
print("Set after discarding 10:", my_set)