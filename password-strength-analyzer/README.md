# Password Strength Analyzer 🔐

A **Python CLI tool** to evaluate the strength of passwords and provide actionable feedback.  
It checks common password rules, estimates entropy, calculates brute-force crack time, detects keyboard patterns, and displays a visual strength meter with colored output.  

This project is perfect for **beginner cybersecurity enthusiasts**, **portfolio GitHub projects**, and **internship preparation**.  

---

## Features

✅ **Password Strength Evaluation**  
- Checks password length (≥12 characters)  
- Detects uppercase, lowercase, digits, and special characters  

✅ **Password Strength Meter Bar**  
- Visual meter `[██████░░░░░░░░░░]`  
- Colored output (red → weak, green → strong)  

✅ **Entropy Calculation**  
- Calculates password entropy in bits using Shannon formula  
- Helps understand how unpredictable your password is  

✅ **Brute-Force Crack Time Estimation**  
- Estimates how long it would take an attacker to crack the password  
- Outputs in seconds, minutes, hours, days, years  

✅ **Common Password Detection**  
- Detects passwords from a common password list (`common_passwords.txt`)  

✅ **Keyboard Pattern Detection**  
- Detects simple sequences like `qwerty`, `123456`, `asdfgh`  

✅ **Suggestions for Improvement**  
- Provides actionable tips to make your password stronger  

---

## Example Output

```text
Enter your password: qwerty123

Analyzing password...

⚠️ This password appears in common password dictionaries and is highly insecure.
⚠️ Password contains common pattern: qwerty
Password Strength Meter: [████████░░░░░░░░░░░░]
Password Strength: Weak
Entropy: 46.53 bits
Estimated Brute Force Crack Time: 1.18 days

Suggestions to improve your password:
- Use at least 12 characters
- Add uppercase letters
- Add special characters