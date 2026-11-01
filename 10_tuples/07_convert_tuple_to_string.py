"""
Q7: Convert a tuple of characters into a single string without str.join().
"""

def tuple_to_string(char_tuple):
    res = ""
    for ch in char_tuple:
        res += str(ch)
    return res

if __name__ == "__main__":
    t = ('P', 'y', 't', 'h', 'o', 'n')
    print("Converted string:", tuple_to_string(t))
