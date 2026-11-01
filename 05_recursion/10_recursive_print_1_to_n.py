"""
Q10: Print numbers from 1 to N and N to 1 using recursion.
Constraint: No loops.
"""

def print_1_to_n(n):
    if n <= 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

def print_n_to_1(n):
    if n <= 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

if __name__ == "__main__":
    print("1 to 7:")
    print_1_to_n(7)
    print()
    print("7 to 1:")
    print_n_to_1(7)
    print()
