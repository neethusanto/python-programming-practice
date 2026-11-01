"""
Q11: Split a string by multiple delimiters like comma, semicolon, pipe, or colon.
"""
import re

def split_by_delimiters(text):
    pattern = r'[,;:|]\s*'
    return re.split(pattern, text)

if __name__ == "__main__":
    text = "apple, banana; cherry| dates: elderberry"
    print("Split items:", split_by_delimiters(text))
