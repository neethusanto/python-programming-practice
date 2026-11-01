"""
Q4: Create a lambda function to find maximum between two numbers without max().
"""

find_max = lambda a, b: a if a >= b else b

if __name__ == "__main__":
    print("Max of (45, 89):", find_max(45, 89))
    print("Max of (100, 20):", find_max(100, 20))
