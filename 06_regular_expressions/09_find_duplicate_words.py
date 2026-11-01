"""
Q9: Find consecutive duplicate words in a sentence using regex backreferences.
"""
import re

def find_duplicate_words(text):
    pattern = r'\b(\w+)\s+\1\b'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return matches

if __name__ == "__main__":
    sentence = "This is is a test test string for for regex duplication test."
    print("Duplicate words:", find_duplicate_words(sentence))
