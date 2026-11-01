"""
Q11: Check if a key exists in a dictionary without using 'key in dict' or dict.has_key().
"""

def key_exists(d, target):
    for k in d:
        if k == target:
            return True
    return False

if __name__ == "__main__":
    info = {"brand": "Toyota", "model": "Corolla", "year": 2022}
    print("'model' exists:", key_exists(info, "model"))
    print("'color' exists:", key_exists(info, "color"))
