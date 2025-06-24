contacts = []

def show_menu():
    print("\n=== CONTACT BOOK MENU ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts to display.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False

    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break

    if not found:
        print("❌ No contact found with that keyword.")

def update_contact():
    name = input("Enter name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep existing value.")
            contact['phone'] = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"New Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"New Address ({contact['address']}): ") or contact['address']
            print("✅ Contact updated successfully!")
            return

    print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            return

    print("❌ Contact not found.")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
