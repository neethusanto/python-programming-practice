"""
Q13: Replace all occurrences of an old character with a new character without using str.replace().
"""

def replace_char(s, old_char, new_char):
    result = ""
    for ch in s:
        if ch == old_char:
            result += new_char
        else:
            result += ch
    return result

if __name__ == "__main__":
    text = "banana"
    print(f"Replace 'a' with 'o' in '{text}':", replace_char(text, 'a', 'o'))
