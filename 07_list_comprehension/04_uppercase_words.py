"""
Q4: Convert a list of lowercase string words to uppercase using list comprehension.
Constraint: Using ASCII character conversion without str.upper().
"""

def to_upper_word(w):
    return "".join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in w])

def uppercase_list(words):
    return [to_upper_word(w) for w in words]

if __name__ == "__main__":
    sample = ["python", "basics", "list", "comprehension"]
    print("Uppercase words:", uppercase_list(sample))
