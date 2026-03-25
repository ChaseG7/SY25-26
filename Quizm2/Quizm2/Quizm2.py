count = 0
letter = input("Enter a letter: ")
for l in "banana":
    if l == letter:
        count += 1
print("The letter", letter, "appears", count, "times in 'banana'.")

guess_count = 0
guess = input("Guess a number between 1 and 10: ")
while guess != "3":
    guess_count += 1
    guess = input("Wrong! Try again: ")
print("Correct! You guessed it in", guess_count + 1, "tries.")
