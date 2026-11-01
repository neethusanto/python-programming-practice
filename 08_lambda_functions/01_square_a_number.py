"""
Q1: Create a lambda function to calculate the square of a number.
"""

square = lambda x: x * x

if __name__ == "__main__":
    for val in [3, 7, 12, -5]:
        print(f"Square of {val} = {square(val)}")
