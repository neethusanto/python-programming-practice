"""
Q8: Write a function to sort a list using bubble sort algorithm without sort() or sorted().
"""

def bubble_sort(items):
    # Create copy manually
    arr = []
    for x in items:
        arr.append(x)
        
    n = 0
    for _ in arr:
        n += 1
        
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr

if __name__ == "__main__":
    original = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted:", bubble_sort(original))
