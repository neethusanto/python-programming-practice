"""
Q7: Remove a key from a dictionary without using pop() or del keyword.
"""

def remove_key(d, target_key):
    new_d = {}
    for k in d:
        if k != target_key:
            new_d[k] = d[k]
    return new_d

if __name__ == "__main__":
    data = {"id": 1, "name": "Sam", "temp": "ignore"}
    print("Cleaned dictionary:", remove_key(data, "temp"))
