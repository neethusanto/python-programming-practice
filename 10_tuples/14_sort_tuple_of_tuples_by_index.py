"""
Q14: Sort a tuple of tuples based on a specified index without using sorted().
"""

def sort_nested_tuples(data, index):
    arr = [x for x in data]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][index] > arr[j + 1][index]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return tuple(arr)

if __name__ == "__main__":
    students = (("John", 88), ("Alice", 95), ("Bob", 72), ("Zara", 91))
    print("Sorted by score:", sort_nested_tuples(students, 1))
