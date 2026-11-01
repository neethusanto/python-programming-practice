"""
Q9: Sort a dictionary by its keys using bubble sort without sorted() or OrderedDict.
"""

def sort_by_keys(d):
    keys = [k for k in d]
    n = len(keys)
    for i in range(n):
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
                
    sorted_dict = {}
    for k in keys:
        sorted_dict[k] = d[k]
    return sorted_dict

if __name__ == "__main__":
    d = {"banana": 3, "apple": 5, "cherry": 2, "date": 8}
    print("Sorted by key:", sort_by_keys(d))
