"""
Q4: Reverse an integer using while loop and modulo/division.
Constraint: No string conversion, no [::-1], no reversed().
"""

def reverse_number(n):
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n = n // 10
        
    return -rev if is_negative else rev

if __name__ == "__main__":
    for val in [12345, -987, 1000, 7]:
        print(f"Reverse of {val} -> {reverse_number(val)}")
