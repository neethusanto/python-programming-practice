"""
Q5: Find Greatest Common Divisor (GCD) using Euclidean recursion.
Constraint: No loops, no math.gcd().
"""

def gcd(a, b):
    if b == 0:
        return a if a >= 0 else -a
    return gcd(b, a % b)

if __name__ == "__main__":
    print("GCD(48, 18) =", gcd(48, 18))
    print("GCD(101, 103) =", gcd(101, 103))
    print("GCD(56, 98) =", gcd(56, 98))
