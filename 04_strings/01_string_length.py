"""
Q1: Find the length of a string without using len().
"""

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

if __name__ == "__main__":
    for word in ["hello", "", "Python Basics", "antigravity"]:
        print(f"Length of '{word}': {string_length(word)}")
