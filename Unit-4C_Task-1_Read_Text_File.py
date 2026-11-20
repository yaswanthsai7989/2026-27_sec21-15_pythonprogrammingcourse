# Create a file
f = open("sample.txt", "w")
f.write("Welcome to Python Programming")
f.close()

# Read data from file
f = open("sample.txt", "r")
data = f.read()

print("File Content:")
print(data)

f.close()