"""
Q2: Invert a dictionary (swap keys and values) without dict comprehension.
"""

def invert_dict(d):
    inverted = {}
    for k in d:
        val = d[k]
        inverted[val] = k
    return inverted

if __name__ == "__main__":
    original = {"name": "Alice", "role": "Engineer", "id": 101}
    print("Inverted:", invert_dict(original))
