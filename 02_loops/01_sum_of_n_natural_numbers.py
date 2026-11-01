"""
Q1: Find the sum of first N natural numbers using a loop.
Constraint: Do not use sum() or range math formula n*(n+1)//2.
"""

def sum_natural_numbers(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

if __name__ == "__main__":
    for n in [5, 10, 100]:
        print(f"Sum of first {n} numbers: {sum_natural_numbers(n)}")
