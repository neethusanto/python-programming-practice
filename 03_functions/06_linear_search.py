"""
Q6: Write a function implementing linear search without using list.index() or 'in'.
Returns index if found, else -1.
"""

def linear_search(items, target):
    idx = 0
    for item in items:
        if item == target:
            return idx
        idx += 1
    return -1

if __name__ == "__main__":
    arr = [10, 25, 30, 45, 50]
    print("Index of 30:", linear_search(arr, 30))
    print("Index of 99:", linear_search(arr, 99))
