"""
Q9: Sort a list of strings by their string length using a lambda key.
"""

def sort_by_length(strings):
    arr = [s for s in strings]
    n = len(arr)
    str_len = lambda s: sum(1 for _ in s)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if str_len(arr[j]) > str_len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    words = ["elephant", "ox", "cat", "hippopotamus", "tiger"]
    print("Sorted by length:", sort_by_length(words))
