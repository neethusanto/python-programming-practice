"""
Q11: Create a lambda function to check if a string is a palindrome.
"""

is_palindrome = lambda s: (lambda rev: s == rev)("".join([s[len(s) - 1 - i] for i in range(len(s))]))

if __name__ == "__main__":
    for word in ["radar", "python", "level", "world"]:
        print(f"'{word}' is palindrome:", is_palindrome(word))
