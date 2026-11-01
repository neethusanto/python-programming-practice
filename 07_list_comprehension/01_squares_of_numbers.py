"""
Q1: Generate squares of numbers from 1 to N using list comprehension.
"""

def generate_squares(n):
    return [x * x for x in range(1, n + 1)]

if __name__ == "__main__":
    print("Squares up to 10:", generate_squares(10))
