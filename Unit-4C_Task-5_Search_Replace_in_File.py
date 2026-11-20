# Read file content
f = open("sample.txt", "r")
data = f.read()
f.close()

# Search and replace word
old = input("Enter word to search: ")
new = input("Enter replacement word: ")

data = data.replace(old, new)

# Write updated content
f = open("sample.txt", "w")
f.write(data)
f.close()

print("Word replaced successfully")
print("Updated Content:")
print(data)