import random

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

# Function to generate a random prime number
def generate_prime():
    while True:
        prime_candidate = random.randint(2**7, 2**8) # Choose a random number between 2^7 and 2^8
        if is_prime(prime_candidate):
            return prime_candidate

# Function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate public and private keys
def generate_keys():
    # Generate two random prime numbers
    p = generate_prime()
    q = generate_prime()

    # Calculate n and φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose e such that 1 < e < φ(n) and e is coprime with φ(n)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calculate d such that (d * e) % φ(n) = 1
    d = pow(e, -1, phi_n)

    # Return public and private keys
    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

# Function to decrypt a message
def decrypt(encrypted_msg, private_key):
    d, n = private_key
    decrypted_msg = [chr(pow(char, d, n)) for char in encrypted_msg]
    return ''.join(decrypted_msg)

# Generate public and private keys
public_key, private_key = generate_keys()
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Message to be encrypted
message = "Hello, RSA!"

# Encrypt the message
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
