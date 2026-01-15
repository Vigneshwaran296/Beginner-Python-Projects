import random
import string


def generate_password():
    print("---Simple Password Generator---")
    # we want to make sure the user inputs a valid number and that it's within the specified range.
    try:
        length = int(input("Enter password length (8-16): "))
        if not (8 <= length <= 16):
            print("Error: Length must be between 8 and 16.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # 2. Get user preferences
    include_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    include_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_digits = input("Include numbers? (y/n): ").lower() == "y"
    include_special = (
        input("Include special characters (symbols)? (y/n): ").lower() == "y"
    )

    # 3. Build the character pool - we are using string.ascii for all lowercase letters, uppercase letters, numbers and special characters.

    char_pool = ""
    if include_lower:
        char_pool += string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    if include_upper:
        char_pool += string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_digits:
        char_pool += string.digits  # "012345678"
    if include_special:
        char_pool += string.punctuation  # "!@#$%^&*()_+-=[]
    # 4. Check if at least one option was selected
    if not char_pool:
        print("Error: You must select at least one character type!")
        return

    # 5. Generate the password
    # Using random.SystemRandom() for cryptographically strong generation

    # print(char_pool) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    password = "".join(random.SystemRandom().choice(char_pool) for i in range(length))

    print(f"\n Generated Password: {password}\n")


if __name__ == "__main__":
    generate_password()
