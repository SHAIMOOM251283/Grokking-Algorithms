import socket

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
    
    def lookup(self, key):
        index = self.hash_function(key)
        return self.table[index]

def resolve_dns(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        print(f"Error resolving DNS for {domain_name}: {e}")
        return None

def main():
    dns_table = HashTable(size=100)  # Size of the hash table

    while True:
        action = input("Enter 'insert' to add a DNS record, 'lookup' to find an IP address, or 'quit' to exit: ").strip().lower()

        if action == 'insert':
            domain_name = input("Enter the domain name: ").strip()
            ip_address = resolve_dns(domain_name)
            if ip_address:
                dns_table.insert(domain_name, ip_address)
                print(f"DNS record inserted: {domain_name} -> {ip_address}")
            else:
                print(f"Failed to resolve DNS for {domain_name}")

        elif action == 'lookup':
            domain_name = input("Enter the domain name to lookup: ").strip()
            ip_address = dns_table.lookup(domain_name)
            if ip_address:
                print(f"The IP address of {domain_name} is: {ip_address}")
            else:
                print(f"Domain name {domain_name} not found in DNS table.")

        elif action == 'quit':
            print("Exiting...")
            break

        else:
            print("Invalid action. Please enter 'insert', 'lookup', or 'quit'.")

if __name__ == "__main__":
    main()
