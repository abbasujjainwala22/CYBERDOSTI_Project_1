# PASSWORD GENERATOR
A very basic python code which helps you generate password on your requirements for length, alphabets, numbers and special characters

## Password Generator

This is a simple password generator written in Python. It allows you to generate a random password of a specified length and character set.

# Description

The 'generate_password' function generates a random password. The user can specify the length of the password and whether it should contain letters, digits, and punctuation.

# How to Use

1. Import the function into your Python script using 'from password_generator import generate_password'.
2. Call the function with your desired parameters. For example, 'generate_password(12, True, True, True)' will generate a 12-character password with letters, digits, and punctuation.

# Code Structure

The code consists of a single function, 'generate_password'. This function takes four parameters:
- 'length': The length of the password to generate.
- 'has_letters': Whether the password should contain letters. Defaults to True.
- 'has_digits': Whether the password should contain digits. Defaults to True.
- 'has_punctuation': Whether the password should contain punctuation. Defaults to True.

# Usage

Here's an example of how to use the password generator:

```python
from password_generator import generate_password

Generate a 12-character password with letters, digits, and punctuation
password = generate_password(12, True, True, True)
print(password)
