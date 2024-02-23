import hashlib

def generate_sha256_hash(string):
    """
    Generates the SHA-256 hash for the given string.

    Args:
    - string: The string to generate the hash for.

    Returns:
    - hash_value: The SHA-256 hash value for the string.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(string.encode())
    return sha256_hash.hexdigest()

# Example usage:
string1 = "Hello, world!"
string2 = "Hello, world!"  # Same content as string1

# Generate SHA-256 hashes for the strings
hash1 = generate_sha256_hash(string1)
hash2 = generate_sha256_hash(string2)

# Compare the hashes to determine if the strings are the same
if hash1 == hash2:
    print("The strings are the same.")
else:
    print("The strings are different.")
