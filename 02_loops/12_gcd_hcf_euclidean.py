"""
Q12: Find Greatest Common Divisor (GCD/HCF) of two numbers using while loop.
Constraint: No math.gcd().
"""

def find_gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

if __name__ == "__main__":
    print("GCD of 48 and 18:", find_gcd(48, 18))
    print("GCD of 101 and 103:", find_gcd(101, 103))
    print("GCD of 56 and 98:", find_gcd(56, 98))
