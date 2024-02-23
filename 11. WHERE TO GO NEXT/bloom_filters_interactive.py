import math
import mmh3  # You may need to install this library via pip (pip install mmh3)

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = [False] * size

    def add(self, item):
        for i in range(self.hash_functions):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = True

    def contains(self, item):
        for i in range(self.hash_functions):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False
        return True

def main():
    size = int(input("Enter size of Bloom Filter: "))
    hash_functions = int(input("Enter number of hash functions: "))
    bloom_filter = BloomFilter(size=size, hash_functions=hash_functions)
    print("Bloom Filter initialized.")

    while True:
        print("\n1. Add an item")
        print("2. Check membership of an item")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            bloom_filter.add(item)
            print(f"Item '{item}' added to Bloom Filter.")
        elif choice == "2":
            item = input("Enter the item to check: ")
            if bloom_filter.contains(item):
                print(f"Item '{item}' may be in the Bloom Filter.")
            else:
                print(f"Item '{item}' is not in the Bloom Filter.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
