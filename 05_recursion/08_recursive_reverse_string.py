"""
Q8: Reverse a string using recursion.
Constraint: No [::-1], no reversed(), no loops.
"""

def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    for text in ["hello", "Python", "Recursion", "a"]:
        print(f"Reverse of '{text}': '{reverse_string(text)}'")
