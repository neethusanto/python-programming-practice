"""
Q15: Flatten a nested dictionary into dot-separated keys without external packages.
"""

def flatten_dict(d, parent_key="", sep="."):
    items = {}
    for k in d:
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(d[k], dict):
            sub_items = flatten_dict(d[k], new_key, sep=sep)
            for sub_k in sub_items:
                items[sub_k] = sub_items[sub_k]
        else:
            items[new_key] = d[k]
    return items

if __name__ == "__main__":
    nested = {
        "user": {
            "name": "Jane",
            "address": {
                "city": "Boston",
                "zip": "02101"
            }
        },
        "status": "active"
    }
    print("Flattened dictionary:", flatten_dict(nested))
