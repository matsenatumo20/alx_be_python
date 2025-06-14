def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            return f"Item '{item}' added to the list."
            pass

        elif choice == "2":
            if not shopping_list:
                return "Item is not found"
            else:
                print = input("Current_list:", shopping_list)
                item = input("Enter the item to remove")
                shopping_list.remove(item)
                return f"Item '{item}' removed from the list."
            pass
                
        elif choice == "3":
            if not shopping_list:
                return "The list is empty"
            else:
                print("Current_list:", shopping_list)
            pass

        elif choice == "4":
            return "Goodbye!"
            break
        else:
            return "Invalid choice. Please try again."
