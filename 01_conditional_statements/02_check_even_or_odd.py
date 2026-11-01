"""
Q2: Check whether an integer is even or odd without using built-in methods.
Constraint: Basic arithmetic operators only.
"""

def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    for num in [12, 17, 0, -5]:
        print(f"{num} is {is_even_or_odd(num)}")
