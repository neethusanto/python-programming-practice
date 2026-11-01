"""
Q2: Calculate factorial of a non-negative integer using a loop.
Constraint: No math.factorial().
"""

def factorial(n):
    if n < 0:
        return None
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == "__main__":
    for n in [0, 1, 5, 7]:
        print(f"{n}! = {factorial(n)}")
