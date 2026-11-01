"""
Q2: Find maximum and minimum numeric elements in a tuple without max() or min().
"""

def max_min_tuple(tup):
    if not tup:
        return None, None
    min_val = tup[0]
    max_val = tup[0]
    for x in tup:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return max_val, min_val

if __name__ == "__main__":
    t = (45, 12, 89, 3, 99, 24)
    print("Max & Min:", max_min_tuple(t))
