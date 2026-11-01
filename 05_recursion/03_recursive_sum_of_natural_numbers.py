"""
Q3: Calculate sum of first N natural numbers using recursion.
Constraint: No loop, no sum().
"""

def sum_natural(n):
    if n <= 0:
        return 0
    return n + sum_natural(n - 1)

if __name__ == "__main__":
    for val in [5, 10, 15]:
        print(f"Sum of first {val} numbers = {sum_natural(val)}")
