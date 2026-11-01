"""
Q11: Implement binary search on a sorted list using recursion.
Constraint: No loops, no bisect.
"""

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Index of 23:", binary_search_recursive(data, 23, 0, len(data) - 1))
    print("Index of 50:", binary_search_recursive(data, 50, 0, len(data) - 1))
