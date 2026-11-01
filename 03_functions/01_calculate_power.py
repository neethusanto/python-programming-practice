"""
Q1: Write a function to calculate base^exponent (power) without using ** or pow().
Handles positive, zero, and negative integer exponents.
"""

def power(base, exp):
    if exp == 0:
        return 1.0
    
    is_neg = False
    if exp < 0:
        is_neg = True
        exp = -exp
        
    result = 1.0
    i = 0
    while i < exp:
        result *= base
        i += 1
        
    return 1.0 / result if is_neg else result

if __name__ == "__main__":
    print("2 ^ 3 =", power(2, 3))
    print("5 ^ 0 =", power(5, 0))
    print("2 ^ -2 =", power(2, -2))
