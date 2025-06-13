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
            return "Add Item"
        elif choice == "2":
            return "Remove Item"
        elif choice == "3":
            return "View List"
        elif choice == "4":
            return "Goodbye!"
        else:
            return "Invalid choice. Please try again."
