"""
Q15: Convert a list/tuple of key-value pair tuples to a dictionary without dict() constructor.
"""

def tuples_to_dict(pairs):
    result = {}
    for pair in pairs:
        key = pair[0]
        value = pair[1]
        result[key] = value
    return result

if __name__ == "__main__":
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    print("Dictionary:", tuples_to_dict(pairs))
