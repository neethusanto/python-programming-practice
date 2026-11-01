"""
Q15: Count occurrences of a specific element in a list using recursion.
Constraint: No loops, no list.count().
"""

def count_occurrences(items, target):
    if not items:
        return 0
    match = 1 if items[0] == target else 0
    return match + count_occurrences(items[1:], target)

if __name__ == "__main__":
    nums = [1, 3, 7, 3, 8, 3, 9, 3, 2]
    print("Occurrences of 3:", count_occurrences(nums, 3))
    print("Occurrences of 5:", count_occurrences(nums, 5))
