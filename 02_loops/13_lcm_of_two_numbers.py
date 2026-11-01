"""
Q13: Find Least Common Multiple (LCM) of two numbers using a loop.
Constraint: No math.lcm().
"""

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    gcd_val = find_gcd(a, b)
    # LCM(a, b) = (|a * b|) // GCD(a, b)
    product = a * b
    if product < 0:
        product = -product
    return product // gcd_val

if __name__ == "__main__":
    print("LCM of 12 and 18:", find_lcm(12, 18))
    print("LCM of 15 and 25:", find_lcm(15, 25))
    print("LCM of 7 and 13:", find_lcm(7, 13))
