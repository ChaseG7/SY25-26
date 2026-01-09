# This is a simple program to calculate a user's age category based on their input.
# It contains a few bugs that need to be fixed.


# Function to determine the age category
def get_age_category(age):
  # Ensure age is an integer and valid
  try:
    age = int(age)
    if age < 1:
      print("Please enter a valid age as a positive number.")
      return None
  except ValueError:
    print("Please enter a valid age as a number.")
    return None

  # Correct age category logic
  if age < 18:
    return "Child"
  elif age < 65:
    return "Adult"
  else:
    return "Senior"


# Main part of the program
def main():
  # Bug 3: Incorrect variable assignment and type conversion.
  # The user input needs to be correctly converted to a number.
  user_age = input("Please enter your age: ")


  category = get_age_category(user_age)


  # Bug 4: Incorrect f-string usage.
  # The program should correctly format the output string.
  if category:
    print(f"You are a {category}.")


# Call the main function to run the program
main()
