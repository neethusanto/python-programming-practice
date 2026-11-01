"""
Q4: Find the key with the minimum numeric value without using min().
"""

def min_value_key(d):
    min_k = None
    min_v = None
    for k in d:
        val = d[k]
        if min_v is None or val < min_v:
            min_v = val
            min_k = k
    return min_k, min_v

if __name__ == "__main__":
    prices = {"apple": 50, "banana": 20, "cherry": 75, "dates": 30}
    k, v = min_value_key(prices)
    print(f"Lowest Price Item: {k} at ${v}")
