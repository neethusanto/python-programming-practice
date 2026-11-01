"""
Q1: Calculate factorial of a number using recursion.
Constraint: No loops, no math.factorial().
"""

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    for n in [0, 1, 5, 6]:
        print(f"{n}! = {factorial(n)}")
