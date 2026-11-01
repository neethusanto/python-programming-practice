"""
Q10: Validate strong password: at least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char.
"""
import re

def is_strong_password(password):
    # Positive lookaheads for conditions
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

if __name__ == "__main__":
    passwords = ["Pass123!", "weakpass", "NoDigit!", "Short1!", "Valid@Code2026"]
    for p in passwords:
        print(f"'{p}' is strong:", is_strong_password(p))
