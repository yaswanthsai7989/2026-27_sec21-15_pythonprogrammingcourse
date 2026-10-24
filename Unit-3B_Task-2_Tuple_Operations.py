#Write a python program to demonstrate tuple operations (concatenation, slicing, unpacking)
my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
# Concatenation
concatenated_tuple = my_tuple1 + my_tuple2
print("Concatenated tuple:", concatenated_tuple)
# Slicing
sliced_tuple = my_tuple1[1:3]
print("Sliced tuple:", sliced_tuple)
# Unpacking
a, b, c = my_tuple1
print("Unpacked values:", a, b, c)