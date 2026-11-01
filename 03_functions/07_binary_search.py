"""
Q7: Write a function implementing binary search on a sorted list without bisect.
Returns index if found, else -1.
"""

def binary_search(sorted_items, target):
    low = 0
    # Manual length calculation without len()
    high = 0
    for _ in sorted_items:
        high += 1
    high -= 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

if __name__ == "__main__":
    arr = [5, 12, 19, 23, 45, 67, 89]
    print("Binary search 23:", binary_search(arr, 23))
    print("Binary search 100:", binary_search(arr, 100))
