import string

def build_pool(use_alpha_lower, use_alpha_upper, use_integer, use_symbols):
    char_pool = ""
    if use_alpha_lower:
        char_pool += string.ascii_lowercase
    if use_alpha_upper:
        char_pool += string.ascii_uppercase
    if use_integer:
        char_pool += string.digits
    if use_symbols:
        char_pool += '`~!@#$%^&*()-_=+\\|]}[{;:\',./<>?'

    return char_pool

print("Use alpha lower: ", build_pool(True, False, False, False))
print ("Use alpha upper: ", build_pool(False, True, False, False))
print ("Use integer: ", build_pool(False, False, True, False))
print ("Use symbols: ", build_pool(False, False, False, True))

