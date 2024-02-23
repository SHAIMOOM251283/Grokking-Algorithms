import random

# Publicly agreed prime number and base
prime = 23
base = 5

# Alice's private key
private_key_alice = random.randint(2, prime - 2)  # A random integer between 2 and prime-2

# Bob's private key
private_key_bob = random.randint(2, prime - 2)  # A random integer between 2 and prime-2

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
