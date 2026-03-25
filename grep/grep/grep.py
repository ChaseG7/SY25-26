file_name = input("Enter the file name: ")
pattern = input("Enter the pattern: ")

file = open(file_name, "r")
lines = file.readlines()

for line in lines:
    if pattern in line:
        print(line.strip())  