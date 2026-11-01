"""
Q6: Remove all special characters/punctuation from a string, keeping only alphanumeric and spaces.
"""
import re

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, '', text)

if __name__ == "__main__":
    sample = "Hello, World! @Python #Basics 2026: Let's code & build."
    print("Cleaned string:", remove_special_characters(sample))
