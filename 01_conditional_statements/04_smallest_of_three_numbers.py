"""
Q4: Find the smallest among three numbers without using min().
Constraint: Using nested or sequential if-elif conditions.
"""

def smallest_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

if __name__ == "__main__":
    print("Smallest (10, 45, 23):", smallest_of_three(10, 45, 23))
    print("Smallest (99, 12, 55):", smallest_of_three(99, 12, 55))
    print("Smallest (-5, -2, -10):", smallest_of_three(-5, -2, -10))
