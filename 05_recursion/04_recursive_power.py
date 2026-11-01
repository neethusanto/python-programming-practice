"""
Q4: Calculate base^exp using recursion without ** or pow().
Handles positive and negative exponents.
"""

def power(base, exp):
    if exp == 0:
        return 1.0
    if exp < 0:
        return 1.0 / power(base, -exp)
    return base * power(base, exp - 1)

if __name__ == "__main__":
    print("2 ^ 5 =", power(2, 5))
    print("3 ^ 0 =", power(3, 0))
    print("2 ^ -3 =", power(2, -3))
