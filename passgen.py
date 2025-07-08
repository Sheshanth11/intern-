import random
import string

# Function to generate password
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define character sets
    letters = string.ascii_letters      
    digits = string.digits              
    symbols = string.punctuation        

    # Combine all characters
    all_characters = letters + digits + symbols

    # Randomly select characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
