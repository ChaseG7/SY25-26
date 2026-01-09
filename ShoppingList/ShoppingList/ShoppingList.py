print("Welcome to the Shopping List Manager!")
print("1. Add Item")
print("2. View Items")
print("3. Remove Item")
print("4. Exit")

shopping_list = []
while True:
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to your shopping list.")
    elif choice == '2':
        if shopping_list:
            print("Your Shopping List:")
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        else:
            print("Your shopping list is empty.")
    elif choice == '3':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list.")
        else:
            print(f"{item} is not in your shopping list.")
    elif choice == '4':
        print("Exiting the Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")