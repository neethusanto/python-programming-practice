"""
Q6: Convert all uppercase characters to lowercase without using str.lower().
ASCII logic: 'A'-'Z' (65-90) -> add 32 -> 'a'-'z' (97-122).
"""

def to_lowercase(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            ascii_val = ord(ch) + 32
            result += chr(ascii_val)
        else:
            result += ch
    return result

if __name__ == "__main__":
    print(to_lowercase("HELLO world! 123"))
