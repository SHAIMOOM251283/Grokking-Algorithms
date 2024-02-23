# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to get prime number from user input
def get_prime():
    while True:
        prime = int(input("Enter a prime number (greater than 3): "))
        if is_prime(prime):
            return prime
        else:
            print("Please enter a prime number.")

# Get prime number from user
prime = get_prime()

# Get base from user
base = int(input("Enter a base (primitive root modulo " + str(prime) + "): "))

# Get private key for Alice
private_key_alice = int(input("Enter Alice's private key (an integer between 2 and " + str(prime - 2) + "): "))

# Get private key for Bob
private_key_bob = int(input("Enter Bob's private key (an integer between 2 and " + str(prime - 2) + "): "))

# Calculate public keys
public_key_alice = (base ** private_key_alice) % prime
public_key_bob = (base ** private_key_bob) % prime

# Exchange public keys

# Assume Alice sends her public key to Bob
received_public_key_alice = public_key_alice

# Assume Bob sends his public key to Alice
received_public_key_bob = public_key_bob

# Calculate shared secret
shared_secret_alice = (received_public_key_bob ** private_key_alice) % prime
shared_secret_bob = (received_public_key_alice ** private_key_bob) % prime

# Both Alice and Bob should have the same shared secret
print("Shared secret computed by Alice:", shared_secret_alice)
print("Shared secret computed by Bob:", shared_secret_bob)
