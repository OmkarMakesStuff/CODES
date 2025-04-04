# contact_book.py

import os

# Function to display the menu
def display_menu():
    print("\n===== Contact Book =====")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Delete a contact")
    print("4. Search a contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    
    # Check if the contact already exists
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            if contact.split(",")[0].strip().lower() == name.lower():
                print("Contact already exists!")
                return
    
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
    print(f"Contact for {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if not os.path.exists("contacts.txt"):
        print("No contacts found.")
        return

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        if contacts:
            print("\n=== All Contacts ===")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    found = False
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            if contact.split(",")[0].strip().lower() != name_to_delete.lower():
                file.write(contact)
            else:
                found = True
    if found:
        print(f"Contact for {name_to_delete} deleted successfully.")
    else:
        print(f"No contact found for {name_to_delete}.")

# Function to search a contact
def search_contact():
    name_to_search = input("Enter the name of the contact to search: ")

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        found = False
        for contact in contacts:
            name, phone = contact.strip().split(",")
            if name.lower() == name_to_search.lower():
                print(f"Found contact: Name: {name}, Phone: {phone}")
                found = True
                break
        if not found:
            print(f"No contact found for {name_to_search}.")

# Main function to run the contact book
def main():
    while True:
        choice = display_menu()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
