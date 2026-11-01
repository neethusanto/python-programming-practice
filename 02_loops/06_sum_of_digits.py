"""
Q6: Find the sum of digits of an integer using arithmetic loop.
Constraint: No str(), no sum(), no map().
"""

def sum_of_digits(n):
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += (n % 10)
        n = n // 10
    return total

if __name__ == "__main__":
    for val in [1234, 999, 5, 0]:
        print(f"Sum of digits in {val}: {sum_of_digits(val)}")
