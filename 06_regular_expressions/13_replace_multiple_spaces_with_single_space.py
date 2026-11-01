"""
Q13: Replace multiple continuous whitespace characters with a single space.
"""
import re

def normalize_whitespace(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)

if __name__ == "__main__":
    text = "Python   Basics   Programming    with     Regular   Expressions."
    print("Normalized:", normalize_whitespace(text))
