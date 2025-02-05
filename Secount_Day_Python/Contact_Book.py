contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def search_contact():
    search_name = input("Enter name to search: ")
    found = [c for c in contacts if search_name.lower() in c['name'].lower()]
    if not found:
        print("No contact found.\n")
        return
    for contact in found:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def delete_contact():
    delete_name = input("Enter name to delete: ")
    global contacts
    contacts = [c for c in contacts if delete_name.lower() != c['name'].lower()]
    print("Contact deleted if existed.\n")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
