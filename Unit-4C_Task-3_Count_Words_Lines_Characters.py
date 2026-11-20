# Open file in read mode
f = open("sample.txt", "r")

data = f.read()

# Count words, lines and characters
words = len(data.split())
lines = len(data.splitlines())
characters = len(data)

print("Words:", words)
print("Lines:", lines)
print("Characters:", characters)

f.close()