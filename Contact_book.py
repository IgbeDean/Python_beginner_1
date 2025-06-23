# creating a simple contact book application using python

# initialize contact book
contact_book = {}

# add name and phone number to contact book
def add_contact():
    while True:
        name = input("Enter name: ").strip()
        if name in contact_book:
            print("That name already exists. Please enter a different name.")
        else:
            break  # Exit the loop if the name is unique

    phone = input("Enter phone number: ").strip()
    contact_book[name] = phone
    print(f"Contact {name} added successfully.")



# display name and phone number in the contact book
def display_contact():
    print("Contact List")
    if not contact_book:
        print("No contact_book found")
    else:
        for name, phone in contact_book.items():
            print(f"{name} has a phone number of {phone}")


# search for a name in the contact book
def search_name():
    name = input("Enter a name to search: ").strip()
    if name in contact_book:
        print(f"{name}'s number is {contact_book[name]}")
    else:
        print("Contact not found")


# to delete a name in the contact book
def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"{name} deleted.")
    else:
        print("Contact not found.")

# show menu
def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View contact_book")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1 - 5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contact()
    elif choice == "3":
        search_name()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")