"""
Q13: Extract all distinct characters from a string as a set without set(string).
"""

def unique_chars(text):
    char_set = set()
    for ch in text:
        char_set.add(ch)
    return char_set

if __name__ == "__main__":
    print("Unique characters in 'banana':", unique_chars("banana"))
