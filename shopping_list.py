
shopping_list = []

while True:
    print("\nadd / remove / show / done")
    choice = input("What would you like to do? ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(item, "has been added to your list.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Shopping list:")
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Please choose add, remove, show, or done.")
