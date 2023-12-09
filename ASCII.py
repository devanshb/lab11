def to_uppercase(letter):
    if 97 <= ord(letter) <= 122:
        return chr(ord(letter) - 32)
    return letter

def to_lowercase(letter):
    if 65 <= ord(letter) <= 90:
        return chr(ord(letter) + 32)
    return letter

def is_alphabet(letter):
    return (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)

def is_digit(character):
    return 48 <= ord(character) <= 57

def is_special_character(character):
    return not is_alphabet(character) and not is_digit(character)

# Example usage
print(to_uppercase('b'))  # Should return 'B'
print(to_lowercase('Q'))  # Should return 'q'
print(is_alphabet('x'))   # Should return True
print(is_digit('4'))      # Should return True
print(is_special_character('@'))  # Should return True
