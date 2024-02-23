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

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    hash1 = generate_sha256_hash(string1)
    hash2 = generate_sha256_hash(string2)

    print(f"SHA-256 hash of '{string1}': {hash1}")
    print(f"SHA-256 hash of '{string2}': {hash2}")

    if hash1 == hash2:
        print("The hashes are the same. The strings are identical.")
    else:
        print("The hashes are different. The strings are different.")

if __name__ == "__main__":
    main()
