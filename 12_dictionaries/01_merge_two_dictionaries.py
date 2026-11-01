"""
Q1: Merge two dictionaries into one without using update() or ** unpack operators.
"""

def merge_dicts(d1, d2):
    merged = {}
    for k in d1:
        merged[k] = d1[k]
    for k in d2:
        merged[k] = d2[k]
    return merged

if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 20, "c": 3}
    print("Merged dictionary:", merge_dicts(dict1, dict2))
