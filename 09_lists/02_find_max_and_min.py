"""
Q2: Find maximum and minimum elements in a list in a single pass without max() or min().
"""

def find_max_min(items):
    if not items:
        return None, None
    min_val = items[0]
    max_val = items[0]
    for x in items:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return max_val, min_val

if __name__ == "__main__":
    arr = [23, 5, 89, -12, 44, 102, 0]
    max_v, min_v = find_max_min(arr)
    print(f"Max: {max_v}, Min: {min_v}")
