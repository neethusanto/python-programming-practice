"""
Q3: Check if a string is a palindrome without using [::-1] or reversed().
"""

def is_palindrome(s):
    length = 0
    for _ in s:
        length += 1
        
    left = 0
    right = length - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    for test in ["madam", "racecar", "python", "abba", "a"]:
        print(f"'{test}' is palindrome: {is_palindrome(test)}")
