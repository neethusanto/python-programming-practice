"""
Q3: Find the largest among three numbers without using max().
Constraint: Using if-elif-else statements.
"""

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    print("Largest (10, 45, 23):", largest_of_three(10, 45, 23))
    print("Largest (99, 12, 55):", largest_of_three(99, 12, 55))
    print("Largest (-5, -2, -10):", largest_of_three(-5, -2, -10))
