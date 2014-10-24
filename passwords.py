import string
import random

def build_pool(use_alpha_lower, use_alpha_upper, use_integer, use_symbols, custom=''):
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
    char_pool += custom

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
    for i in range(int(password_length)):
        password += generator.choice(char_pool)
    return password

# print(generate_password(12, build_pool(True, True, True, True)))

def parse_bool(decision):
    if "y" in decision.lower():
        return True
    else:
        return False

def main():
    password_length = input("Enter the length of the password: ")

    # Menu
    print("--- Character Sets ---")
    print("Lowercase: ", string.ascii_lowercase)
    print("Uppercase: ", string.ascii_lowercase)
    print("Digits: ", string.digits)
    print("Symbols: ", string.punctuation)

    print("Choose character sets to use for random password generation. You can add a custom set too!\n")
    use_alpha_lower = parse_bool(input("Use lowercase letters? (y/n): "))
    use_alpha_upper = parse_bool(input("Use uppercase letters? (y/n): "))
    use_digits = parse_bool(input("Use digits? (y/n): "))
    use_symbols = parse_bool(input("Use symbols? (y/n): "))
    use_custom = parse_bool(input("Would you like to add a custom set? (y/n): "))

    # Allow user to select a custom set. 
    custom_set = ''
    if use_custom:
        custom_set = input("Enter the custom character set: ")

    # Only proceed if at least one character set has been chosen.
    if use_alpha_lower or use_alpha_upper or use_digits or use_symbols or use_custom:
        print(generate_password(password_length, build_pool(use_alpha_lower, use_alpha_upper,
                                                            use_digits, use_symbols,custom=custom_set)))

    else:
        print("You didn't select any character pools! Try again!")
        main()

if __name__ == '__main__':
    main()

