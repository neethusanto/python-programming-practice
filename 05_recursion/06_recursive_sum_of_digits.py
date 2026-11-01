"""
Q6: Find sum of digits of a non-negative integer using recursion.
Constraint: Arithmetic operations only, no str() or loop.
"""

def sum_digits(n):
    if n < 0:
        n = -n
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

if __name__ == "__main__":
    for val in [1234, 987, 5, 0]:
        print(f"Sum of digits in {val} = {sum_digits(val)}")
