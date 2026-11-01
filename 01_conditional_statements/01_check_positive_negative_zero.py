"""
Q1: Check whether a given number is positive, negative, or zero.
Constraint: No built-in methods.
"""

def check_number_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    for val in [15, -7, 0]:
        print(f"{val} is {check_number_sign(val)}")
