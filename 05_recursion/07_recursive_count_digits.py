"""
Q7: Count number of digits in an integer using recursion.
Constraint: No len(), no str(), no loop.
"""

def count_digits(n):
    if n < 0:
        n = -n
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

if __name__ == "__main__":
    for val in [0, 8, 125, 987654]:
        print(f"Digits in {val} = {count_digits(val)}")
