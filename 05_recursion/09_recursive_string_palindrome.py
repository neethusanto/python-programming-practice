"""
Q9: Check if a string is palindrome using recursion.
Constraint: No [::-1], no loops.
"""

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

if __name__ == "__main__":
    for word in ["madam", "racecar", "python", "abba", "x"]:
        print(f"'{word}' is palindrome: {is_palindrome(word)}")
