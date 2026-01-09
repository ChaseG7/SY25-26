def flag():
    for i in range(3):
        print("*****===============")
    for i in range(3):
        print("====================")

print("Hello, World!")
name = input("What is your name? ")
age = int(input("What is your age? "))
if age >= 18:
    print("You can vote!")
    flag()
else:
    print("You can't vote.")