"""
Q13: Combine two dictionaries, adding values for common keys.
"""

def combine_add_dicts(d1, d2):
    combined = {}
    for k in d1:
        combined[k] = d1[k]
    for k in d2:
        if k in combined:
            combined[k] += d2[k]
        else:
            combined[k] = d2[k]
    return combined

if __name__ == "__main__":
    store1 = {"apple": 10, "banana": 5, "orange": 8}
    store2 = {"banana": 12, "orange": 4, "mango": 15}
    print("Combined inventory:", combine_add_dicts(store1, store2))
