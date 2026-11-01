"""
Q14: Sort a list of numbers using bubble sort algorithm without sort() or sorted().
"""

def bubble_sort(items):
    arr = [x for x in items]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    unsorted = [64, 25, 12, 22, 11]
    print("Sorted:", bubble_sort(unsorted))
