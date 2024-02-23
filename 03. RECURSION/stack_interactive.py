class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def print_stack(stack):
    if stack.is_empty():
        print("Stack is empty.")
    else:
        print("Stack:", stack.items)

def main():
    stack = Stack()
    print("Welcome to the Stack CLI!")
    print("Commands:")
    print("  push <value>: Push a value onto the stack")
    print("  pop: Pop the top element from the stack")
    print("  peek: Peek at the top element of the stack")
    print("  exit: Exit the program")

    while True:
        command = input("Enter command: ").strip().lower()

        if command.startswith("push"):
            value = command.split(" ", 1)[-1].strip()
            stack.push(value)
            print("Pushed", value, "onto the stack.")
            print_stack(stack)
        elif command == "pop":
            try:
                popped = stack.pop()
                print("Popped", popped, "from the stack.")
                print_stack(stack)
            except IndexError:
                print("Error: Stack is empty.")
        elif command == "peek":
            top = stack.peek()
            if top is not None:
                print("Top element of the stack:", top)
            else:
                print("Stack is empty.")
        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
