# Create an empty dictionary
book = {}

# Function to add items and their prices
def add_item():
    item = input("Enter the item name: ")
    price = float(input("Enter the price of {}:".format(item)))
    book[item] = price
    print("Item '{}' with price '{}' added successfully.".format(item, price))

# Function to display all items and their prices
def display_book():
    print("Items and their prices:")
    for item, price in book.items():
        print("- {}: ${}".format(item, price))

# Function to display price of a specific item
def display_item_price():
    item = input("Enter the item name to display its price: ")
    if item in book:
        print("Price of '{}': ${}".format(item, book[item]))
    else:
        print("Item '{}' not found in the book.".format(item))

# Main function to handle the CLI
def main():
    while True:
        print("\n1. Add an item")
        print("2. Display all items and prices")
        print("3. Display price of a specific item")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            display_book()
        elif choice == '3':
            display_item_price()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
