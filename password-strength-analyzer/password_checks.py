import re

with open("common_passwords.txt", "r") as file:
    COMMON_PASSWORDS = set(file.read().splitlines())


def check_length(password):
    return len(password) >= 12


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_digits(password):
    return any(char.isdigit() for char in password)


def check_special(password):
    return bool(re.search(r"[^A-Za-z0-9]", password))


def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

# --- Keyboard Pattern Detection ---
KEYBOARD_PATTERNS = [
    "qwerty", "asdfgh", "zxcvbn",
    "123456", "password", "admin",
    "letmein", "welcome", "abc123"
]

def contains_keyboard_pattern(password):
    """
    Checks if the password contains common keyboard patterns or sequences.
    Returns: (True, pattern) if found, else (False, None)
    """
    password_lower = password.lower()
    for pattern in KEYBOARD_PATTERNS:
        if pattern in password_lower:
            return True, pattern
    return False, None