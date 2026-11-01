"""
Q12: Calculate the sum of elements in a list using recursion.
Constraint: No loops, no sum().
"""

def sum_list(items):
    if not items:
        return 0
    return items[0] + sum_list(items[1:])

if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50]
    print("List sum:", sum_list(lst))
