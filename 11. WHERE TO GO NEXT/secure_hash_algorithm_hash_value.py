import hashlib

def calculate_sha256_hash(string):
    """
    Calculates the SHA-256 hash value for the given string.

    Args:
    - string: The string to calculate the hash for.

    Returns:
    - hash_value: The SHA-256 hash value for the string.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(string.encode())
    return sha256_hash.hexdigest()

def main():
    string = input("Enter the string to calculate SHA-256 hash for: ")
    hash_value = calculate_sha256_hash(string)
    print(f"SHA-256 hash of '{string}': {hash_value}")

if __name__ == "__main__":
    main()
