class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def view_queue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", self.items)


def main():
    q = Queue()
    while True:
        print("\nSelect operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if queue is empty")
        print("4. Get size of queue")
        print("5. View queue")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter element to enqueue: ")
            q.enqueue(item)
            print(f"{item} enqueued to the queue.")
        elif choice == "2":
            item = q.dequeue()
            if item is not None:
                print(f"Dequeued item: {item}")
            else:
                print("Queue is empty.")
        elif choice == "3":
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == "4":
            print(f"Size of queue: {q.size()}")
        elif choice == "5":
            q.view_queue()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
