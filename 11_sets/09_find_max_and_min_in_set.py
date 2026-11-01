"""
Q9: Find maximum and minimum elements in a set without max() or min().
"""

def max_min_set(s):
    if not s:
        return None, None
    min_val = None
    max_val = None
    for x in s:
        if min_val is None or x < min_val:
            min_val = x
        if max_val is None or x > max_val:
            max_val = x
    return max_val, min_val

if __name__ == "__main__":
    sample = {24, 7, 91, 15, 63}
    max_v, min_v = max_min_set(sample)
    print(f"Max: {max_v}, Min: {min_v}")
