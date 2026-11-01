"""
Q3: Find the key with the maximum numeric value without using max().
"""

def max_value_key(d):
    max_k = None
    max_v = None
    for k in d:
        val = d[k]
        if max_v is None or val > max_v:
            max_v = val
            max_k = k
    return max_k, max_v

if __name__ == "__main__":
    scores = {"math": 88, "physics": 95, "chemistry": 79, "english": 92}
    k, v = max_value_key(scores)
    print(f"Max Subject: {k} with score {v}")
