import bcrypt

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(password, hashed_password):
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Example usage:
def main():
    # Get password from user input
    password = input("Enter your password: ")

    # Hash the password
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)

    # Simulating password check
    entered_password = input("Enter your password again to check: ")
    if check_password(entered_password, hashed_password):
        print("Password correct!")
    else:
        print("Password incorrect!")

if __name__ == "__main__":
    main()
