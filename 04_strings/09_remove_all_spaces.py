"""
Q9: Remove all spaces from a string without using replace() or split().
"""

def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != ' ' and ch != '\t' and ch != '\n':
            result += ch
    return result

if __name__ == "__main__":
    text = " Python  Programming   Basics  "
    print("Without spaces:", remove_spaces(text))
