"""
Q7: Check if an alphabet character is a vowel or consonant.
Constraint: Handle uppercase and lowercase without lower() or upper().
"""

def check_vowel_consonant(ch):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if ch in vowels:
        return "Vowel"
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        return "Consonant"
    else:
        return "Not an alphabet letter"

if __name__ == "__main__":
    for c in ['e', 'B', 'A', 'z', '9']:
        print(f"'{c}' -> {check_vowel_consonant(c)}")
