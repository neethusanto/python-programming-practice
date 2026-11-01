"""
Q5: Convert all lowercase characters to uppercase without using str.upper().
ASCII logic: 'a'-'z' (97-122) -> subtract 32 -> 'A'-'Z' (65-90).
"""

def to_uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            # chr and ord are Python base functions for ASCII conversion
            ascii_val = ord(ch) - 32
            result += chr(ascii_val)
        else:
            result += ch
    return result

if __name__ == "__main__":
    print(to_uppercase("hello WORLD! 123"))
