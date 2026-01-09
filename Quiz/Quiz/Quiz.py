# Start
print("Welcome to the Animal Quiz!")
score = 0

# Question 1
print("\n1. What animal says 'meow'?")
print("a) Dog")
print("b) Cat")
print("c) Cow")
answer1 = input("Enter your answer (a/b/c): ")
if answer1.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 2
print("\n2. Which animal is the largest?")
print("a) Elephant")
print("b) Whale")
print("c) Giraffe")
answer2 = input("Enter your answer (a/b/c): ")
if answer2.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3
print("\n3. Which of these animals can fly?")
print("a) Penguin")
print("b) Ostrich")
print("c) Eagle")
answer3 = input("Enter your answer (a/b/c): ")
if answer3.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 4
print("\n4. What animal is known as man's best friend?")
print("a) Cat")
print("b) Dog")
print("c) Parrot")
answer4 = input("Enter your answer (a/b/c): ")
if answer4.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 5
print("\n5. Which animal is black and white and eats bamboo?")
print("a) Zebra")
print("b) Panda")
print("c) Skunk")
answer5 = input("Enter your answer (a/b/c): ")
if answer5.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 6
print("\n6. Which animal has a long neck?")
print("a) Giraffe")
print("b) Lion")
print("c) Kangaroo")
answer6 = input("Enter your answer (a/b/c): ")
if answer6.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 7
print("\n7. What do bees make?")
print("a) Milk")
print("b) Honey")
print("c) Juice")
answer7 = input("Enter your answer (a/b/c): ")
if answer7.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 8
print("\n8. What animal lives in water and has gills?")
print("a) Dog")
print("b) Fish")
print("c) Lizard")
answer8 = input("Enter your answer (a/b/c): ")
if answer8.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 9
print("\n9. Which bird repeats what people say?")
print("a) Parrot")
print("b) Chicken")
print("c) Eagle")
answer9 = input("Enter your answer (a/b/c): ")
if answer9.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 10
print("\n10. Which animal hops and has a pouch?")
print("a) Elephant")
print("b) Monkey")
print("c) Kangaroo")
answer10 = input("Enter your answer (a/b/c): ")
if answer10.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Final Score
print("\nYou finished the quiz!")
print("Your score is", score, "out of 20.")
