import random
import string

def generate_password(length=12, use_letters=True, use_symbols=True, use_numbers=True):
    """
    Generate a random password with letters, symbols, and numbers.
    
    Args:
        length: Password length (default: 12)
        use_letters: Include letters (default: True)
        use_symbols: Include symbols (default: True)
        use_numbers: Include numbers (default: True)
    
    Returns:
        A random password string
    """
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    
    if not characters:
        raise ValueError("At least one character type must be enabled")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    # Generate a password with default settings
    pwd = generate_password()
    print(f"Generated Password: {pwd}")
    
    # Generate a longer password
    pwd2 = generate_password(length=16)
    print(f"Generated Password (16 chars): {pwd2}")
    
    # Generate with only letters and numbers
    pwd3 = generate_password(use_symbols=False)
    print(f"Generated Password (letters & numbers): {pwd3}")