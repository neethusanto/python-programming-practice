"""
Q10: Check whether a number is a palindrome using numeric operations.
Constraint: No string conversion, no str(n)[::-1].
"""

def is_palindrome_number(n):
    if n < 0:
        return False
    
    original = n
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    
    return original == rev

if __name__ == "__main__":
    for val in [121, 12321, 1234, 10, 7, -121]:
        print(f"{val} is palindrome: {is_palindrome_number(val)}")
