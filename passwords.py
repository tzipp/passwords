import string
import random

def build_pool(use_alpha_lower, use_alpha_upper, use_integer, use_symbols):
    "Build a pool of characters from which to generate a password."
    char_pool = ""
    if use_alpha_lower:
        char_pool += string.ascii_lowercase
    if use_alpha_upper:
        char_pool += string.ascii_uppercase
    if use_integer:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    return char_pool

# print("Use alpha lower: ", build_pool(True, False, False, False))
# print ("Use alpha upper: ", build_pool(False, True, False, False))
# print ("Use integer: ", build_pool(False, False, True, False))
# print ("Use symbols: ", build_pool(False, False, False, True))

def generate_password(password_length, char_pool):
    "Generate a password from a specified password length and character pool."
    try:
        generator = random.SystemRandom()
    except NotImplementedError:
        print("Warning: Not from cryptographically secure randomness source.")
        generator = random.seed()

    password = ''
    for i in range(password_length):
        random_position = generator.randrange(len(char_pool))
        password += char_pool[random_position]
    return password

# print(generate_password(12, build_pool(True, True, True, True)))

