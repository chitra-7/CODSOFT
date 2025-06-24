import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # All character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    # Ensure at least one character from each group is included
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)

    # Fill the rest of the password length
    password += ''.join(random.choices(all_chars, k=length - 4))

    # Shuffle to make it truly random
    password = ''.join(random.sample(password, len(password)))
    return password

# Main Program
print("=== PASSWORD GENERATOR ===")
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
