# Create a Contact Management System that stores names and phone numbers, with functions to add, search, and display contacts

contacts = {}   

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!\n")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found!")
    print()

def display_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        print("------ Contact List ------")
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")
        print()

# Main program
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        display_contacts()

    elif choice == "4":
        print("Exiting Contact Management System...")
        break

    else:
        print("Invalid choice! Please try again.\n")
