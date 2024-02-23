phone_book = {}

def add_contact():
    contact_name = input("Enter the contact name: ").strip()
    phone_number = input("Enter the phone number: ").strip()
    phone_book[contact_name] = phone_number
    print(f"Contact '{contact_name}' with phone number '{phone_number}' added successfully.")

def display_phone_book():
    print("Phone Book:")
    for contact_name, phone_number in phone_book.items():
        print(f"{contact_name}: {phone_number}")

def display_contact_number():
    contact_name = input("Enter the contact name to display its phone number: ").strip()
    if contact_name in phone_book:
        print(f"Phone number of '{contact_name}': {phone_book[contact_name]}")
    else:
        print(f"Contact '{contact_name}' not found in the phone book.")

def main():
    global phone_book

    while True:
        print("\n1. Add a contact")
        print("2. Display phone book")
        print("3. Display phone number of a specific contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            display_phone_book()
        elif choice == '3':
            display_contact_number()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
