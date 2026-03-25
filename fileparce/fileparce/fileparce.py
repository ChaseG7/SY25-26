from itertools import count

file_name = input("Enter the name of the file to parse: ")
file = open(file_name, "r")
word = input("Enter word to search for: ")
count = 0
line = file.readline()
while line:
    if word in line:
        count += 1
    line = file.readline()
print(f"Searching for '{word}' in {file_name}...")
print(f"{word} appears {count} times in the file.")