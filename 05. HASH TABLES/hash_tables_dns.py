class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        # A simple hash function to determine the index
        # This can be more sophisticated in real implementations
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
    
    def lookup(self, key):
        index = self.hash_function(key)
        return self.table[index]

# Example usage:
dns_table = HashTable(size=100)  # Size of the hash table

# Inserting DNS records into the hash table
dns_table.insert("example.com", "192.0.2.1")
dns_table.insert("google.com", "172.217.6.46")
dns_table.insert("openai.com", "69.195.65.31")

# Looking up IP address for a domain name
domain_name = "google.com"
ip_address = dns_table.lookup(domain_name)
if ip_address:
    print(f"The IP address of {domain_name} is: {ip_address}")
else:
    print(f"Domain name {domain_name} not found in DNS table.")
