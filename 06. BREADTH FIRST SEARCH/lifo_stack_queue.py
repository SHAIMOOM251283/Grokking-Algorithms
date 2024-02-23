class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def view_stack(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents:", self.items)


def main():
    s = Stack()
    while True:
        print("\nSelect operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Check if stack is empty")
        print("4. Get size of stack")
        print("5. View stack")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter element to push: ")
            s.push(item)
            print(f"{item} pushed to the stack.")
        elif choice == "2":
            item = s.pop()
            if item is not None:
                print(f"Popped item: {item}")
            else:
                print("Stack is empty.")
        elif choice == "3":
            if s.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == "4":
            print(f"Size of stack: {s.size()}")
        elif choice == "5":
            s.view_stack()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
