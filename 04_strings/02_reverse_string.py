"""
Q2: Reverse a string without using [::-1] or reversed().
"""

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

if __name__ == "__main__":
    for text in ["hello", "Python", "racecar", "A"]:
        print(f"Reverse of '{text}': '{reverse_string(text)}'")
