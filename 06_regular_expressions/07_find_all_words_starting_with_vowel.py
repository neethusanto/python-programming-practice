"""
Q7: Find all words in a string that begin with a vowel (case-insensitive).
"""
import re

def words_starting_with_vowels(text):
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    sentence = "An eagle flew over an open orange umbrella in India."
    print("Vowel-starting words:", words_starting_with_vowels(sentence))
