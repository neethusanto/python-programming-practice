"""
Q7: Toggle case of each character in a string without swapcase().
"""

def toggle_case(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

if __name__ == "__main__":
    print(toggle_case("PyThOn 3.14 Programming!"))
