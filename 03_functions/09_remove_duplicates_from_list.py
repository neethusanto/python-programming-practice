"""
Q9: Write a function to remove duplicates from a list while preserving order.
Constraint: No set(), dict.fromkeys(), or built-in deduplication methods.
"""

def remove_duplicates(items):
    unique = []
    for item in items:
        found = False
        for u in unique:
            if u == item:
                found = True
                break
        if not found:
            unique.append(item)
    return unique

if __name__ == "__main__":
    data = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    print("Deduplicated list:", remove_duplicates(data))
