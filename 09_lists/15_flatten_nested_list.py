"""
Q15: Flatten an arbitrarily nested list of numbers into a 1D list without third-party libraries.
"""

def flatten_deep(items):
    flat = []
    for x in items:
        if isinstance(x, list):
            for sub in flatten_deep(x):
                flat.append(sub)
        else:
            flat.append(x)
    return flat

if __name__ == "__main__":
    nested = [1, [2, [3, 4], 5], 6, [7, 8]]
    print("Flattened list:", flatten_deep(nested))
