"""
Q7: Sort a list of tuples by their second element using a lambda key.
"""

def sort_by_second_element(tuples_list):
    # Bubble sort using lambda key to avoid built-in sorted()
    arr = [x for x in tuples_list]
    n = len(arr)
    key_func = lambda t: t[1]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(arr[j]) > key_func(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    data = [("apple", 50), ("banana", 20), ("cherry", 75), ("dates", 30)]
    print("Sorted by value:", sort_by_second_element(data))
