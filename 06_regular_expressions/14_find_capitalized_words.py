"""
Q14: Find all words that start with a capital letter followed by lowercase letters.
"""
import re

def find_capitalized_words(text):
    pattern = r'\b[A-Z][a-z]+\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    text = "Alice went to London with Bob and visited Buckingham Palace."
    print("Capitalized words:", find_capitalized_words(text))
