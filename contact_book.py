class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("\nContact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found!")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"\nContact {idx}:\n{contact}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("\nNo contacts found with that search term!")
        else:
            for idx, contact in enumerate(results, 1):
                print(f"\nSearch Result {idx}:\n{contact}")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("\nContact found:")
                print(contact)
                name = input("Enter new name (leave blank to keep current): ") or contact.name
                phone = input("Enter new phone number (leave blank to keep current): ") or contact.phone
                email = input("Enter new email (leave blank to keep current): ") or contact.email
                address = input("Enter new address (leave blank to keep current): ") or contact.address

                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address
                print("\nContact updated successfully!")
                return
        print("\nContact not found!")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("\nContact deleted successfully!")
                return
        print("\nContact not found!")


def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting Contact Book...")
            break

        else:
            print("\nInvalid choice! Please choose a valid option.")


if __name__ == "__main__":
    main()
