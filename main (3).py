import random
import string

def password_generator():
    length = int(input("Enter the desired password length: "))
    
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    character_pool = string.ascii_lowercase
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    print(f"Generated Password: {password}")

password_generator()
