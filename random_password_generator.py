import random
import string

def generate_password(length):
    """Generate a random password of a specified length"""
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure that the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    password = ''
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if (any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and any(char.isdigit() for char in password)
                and any(char in string.punctuation for char in password)):
            break

    return password

# Prompt the user to enter the desired password length
length = int(input("Enter the length of the password: "))

# Generate a random password of the specified length
password = generate_password(length)

# Display the generated password
print("Your password is:", password)