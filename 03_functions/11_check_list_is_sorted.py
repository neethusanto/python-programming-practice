"""
Q11: Write a function to check if a list is sorted in ascending order.
"""

def is_sorted_ascending(items):
    n = 0
    for _ in items:
        n += 1
        
    if n <= 1:
        return True
        
    i = 0
    while i < n - 1:
        if items[i] > items[i + 1]:
            return False
        i += 1
    return True

if __name__ == "__main__":
    print("[1, 2, 3, 4, 5] is sorted:", is_sorted_ascending([1, 2, 3, 4, 5]))
    print("[1, 3, 2, 4, 5] is sorted:", is_sorted_ascending([1, 3, 2, 4, 5]))
