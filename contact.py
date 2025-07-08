import csv

contacts = []  # List to store contact dictionaries

def add_contact():
    name = input("Enter Name: ")
    # Check for duplicates
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(" Contact with this name already exists.\n")
            return
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print(" Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print(" No contacts available.\n")
        return
    print(" Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} |  {contact['phone']} |  {contact['email']} |  {contact['address']}")
    print()

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print(" Contact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print(" Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Enter new details (leave blank to keep existing):")
            phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New Email ({contact['email']}): ") or contact['email']
            address = input(f"New Address ({contact['address']}): ") or contact['address']
            contact.update({"phone": phone, "email": email, "address": address})
            print(" Contact updated successfully!\n")
            return
    print(" Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("️ Contact deleted successfully!\n")
            return
    print(" Contact not found.\n")

def save_contacts_to_file():
    if not contacts:
        print(" No contacts to save.\n")
        return
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
        writer.writeheader()
        writer.writerows(contacts)
    print(" Contacts saved to 'contacts.csv'.\n")

def contact_book():
    while True:
        print(" Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save to File")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            save_contacts_to_file()
        elif choice == "7":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.\n")

# Start the application
contact_book()
