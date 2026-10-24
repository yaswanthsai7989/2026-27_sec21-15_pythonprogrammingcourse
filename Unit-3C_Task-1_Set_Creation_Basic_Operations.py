#Write a python program to demonstrate set creation and basic set operations (union, intersection, difference)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union
union_set = set1.union(set2)
print("Union of sets:", union_set)
# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)
# Difference
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)