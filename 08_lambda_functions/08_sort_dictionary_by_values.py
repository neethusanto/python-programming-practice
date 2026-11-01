"""
Q8: Sort dictionary items by value using a lambda key function.
"""

def sort_dict_by_values(d):
    items = [(k, d[k]) for k in d]
    n = len(items)
    key_func = lambda item: item[1]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(items[j]) > key_func(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

if __name__ == "__main__":
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
    print("Sorted items:", sort_dict_by_values(scores))
