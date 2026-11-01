"""
Q10: Sort a dictionary by its values using bubble sort without sorted().
"""

def sort_by_values(d):
    items = [(k, d[k]) for k in d]
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                
    sorted_dict = {}
    for pair in items:
        sorted_dict[pair[0]] = pair[1]
    return sorted_dict

if __name__ == "__main__":
    d = {"banana": 3, "apple": 5, "cherry": 2, "date": 8}
    print("Sorted by value:", sort_by_values(d))
