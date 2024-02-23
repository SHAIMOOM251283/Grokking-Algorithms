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
    # Get original string from user
    original_string = input("Enter the original string: ")

    # Calculate hash of original string
    original_hash = calculate_sha256_hash(original_string)
    print("Original String:", original_string)
    print("Hash of Original String:", original_hash)

    # User input
    user_input = input("Enter a string to compare with the original: ")

    # Calculate hash of user input
    user_hash = calculate_sha256_hash(user_input)
    print("Hash of User Input:", user_hash)

    # Compare hashes
    if original_hash == user_hash:
        print("The user input matches the original string.")
    else:
        print("The user input does not match the original string.")

if __name__ == "__main__":
    main()
