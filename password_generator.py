import string
import random

def generate_password(length, has_letters=True, has_digits=True, has_punctuation=True):
    characters = ''
    if has_letters:
        characters += string.ascii_letters
    if has_digits:
        characters += string.digits
    if has_punctuation:
        characters += string.punctuation
    if len(characters) == 0:
        return 'Error: No characters to choose from'
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password(16, False, False, False))
