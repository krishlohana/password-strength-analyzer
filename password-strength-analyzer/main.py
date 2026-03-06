from password_checks import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_digits,
    check_special,
    is_common_password,
    contains_keyboard_pattern  # NEW: import keyboard pattern detection
)

from entropy_calculator import calculate_entropy
from crack_time_estimator import estimate_crack_time

from colorama import Fore, Style, init
init()


# Function to show password strength meter bar
def strength_meter_bar(score, max_score=5):
    total_units = 20
    filled_units = int((score / max_score) * total_units)
    empty_units = total_units - filled_units

    if score <= 1:
        color = Fore.RED
    elif score == 2:
        color = Fore.LIGHTRED_EX
    elif score == 3:
        color = Fore.YELLOW
    elif score == 4:
        color = Fore.GREEN
    else:
        color = Fore.LIGHTGREEN_EX

    bar = "[" + "█" * filled_units + "░" * empty_units + "]"
    return color + bar + Style.RESET_ALL


# --- Main Program ---
password = input("Enter your password: ")
print("Analyzing password...\n")

score = 0

length_ok = check_length(password)
upper_ok = check_uppercase(password)
lower_ok = check_lowercase(password)
digit_ok = check_digits(password)
special_ok = check_special(password)

if length_ok:
    score += 1
if upper_ok:
    score += 1
if lower_ok:
    score += 1
if digit_ok:
    score += 1
if special_ok:
    score += 1

# Check common passwords
if is_common_password(password):
    print(Fore.RED + "⚠️ This password appears in common password dictionaries and is highly insecure." + Style.RESET_ALL)

# Check keyboard patterns
pattern_found, pattern = contains_keyboard_pattern(password)
if pattern_found:
    print(Fore.RED + f"⚠️ Password contains common pattern: {pattern}" + Style.RESET_ALL)

# Determine strength label
if score <= 1:
    strength = "Very Weak"
elif score == 2:
    strength = "Weak"
elif score == 3:
    strength = "Moderate"
elif score == 4:
    strength = "Strong"
else:
    strength = "Very Strong"

# Color for strength
if strength == "Very Weak":
    color = Fore.RED
elif strength == "Weak":
    color = Fore.LIGHTRED_EX
elif strength == "Moderate":
    color = Fore.YELLOW
elif strength == "Strong":
    color = Fore.GREEN
else:
    color = Fore.LIGHTGREEN_EX

# Show password strength bar
print("Password Strength Meter:", strength_meter_bar(score))
print("Password Strength:", color + strength + Style.RESET_ALL)

# Entropy and Crack time
entropy = calculate_entropy(password)
print("Entropy:", round(entropy, 2), "bits")

crack_time = estimate_crack_time(entropy)
print("Estimated Brute Force Crack Time:", crack_time)

# Suggestions
suggestions = []
if not length_ok:
    suggestions.append("Use at least 12 characters")
if not upper_ok:
    suggestions.append("Add uppercase letters")
if not lower_ok:
    suggestions.append("Add lowercase letters")
if not digit_ok:
    suggestions.append("Add numbers")
if not special_ok:
    suggestions.append("Add special characters")

if suggestions:
    print("\nSuggestions to improve your password:")
    for s in suggestions:
        print("-", s)