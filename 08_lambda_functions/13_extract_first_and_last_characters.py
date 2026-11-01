"""
Q13: Create a lambda function to extract first and last character of a string as a tuple.
"""

first_and_last = lambda s: (s[0], s[len(s) - 1]) if len(s) > 0 else (None, None)

if __name__ == "__main__":
    for word in ["Python", "Lambda", "A"]:
        print(f"'{word}' ->", first_and_last(word))
