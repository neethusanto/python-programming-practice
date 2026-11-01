"""
Q14: Check whether a character is uppercase, lowercase, digit, or special character
without using isupper(), islower(), isdigit(), etc.
"""

def detect_character_type(ch):
    if 'A' <= ch <= 'Z':
        return "Uppercase Alphabet"
    elif 'a' <= ch <= 'z':
        return "Lowercase Alphabet"
    elif '0' <= ch <= '9':
        return "Digit"
    else:
        return "Special Character / Symbol"

if __name__ == "__main__":
    for c in ['M', 'g', '7', '@', ' ']:
        print(f"'{c}' -> {detect_character_type(c)}")
