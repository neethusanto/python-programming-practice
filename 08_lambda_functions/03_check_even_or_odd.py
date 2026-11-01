"""
Q3: Create a lambda function to determine whether a number is even or odd.
"""

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

if __name__ == "__main__":
    for n in [10, 15, 0, 99]:
        print(f"{n} is {is_even(n)}")
