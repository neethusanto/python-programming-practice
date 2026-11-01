"""
Q14: Check if a list is sorted in ascending order using recursion.
Constraint: No loops, no sort()/sorted().
"""

def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted(arr[1:])

if __name__ == "__main__":
    print("[1, 2, 4, 7, 9] sorted:", is_sorted([1, 2, 4, 7, 9]))
    print("[1, 5, 3, 7, 9] sorted:", is_sorted([1, 5, 3, 7, 9]))
