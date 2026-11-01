"""
Q10: Remove a specific item from a tuple by constructing a new tuple.
"""

def remove_from_tuple(tup, target):
    new_items = []
    removed = False
    for x in tup:
        if x == target and not removed:
            removed = True
            continue
        new_items.append(x)
    return tuple(new_items)

if __name__ == "__main__":
    t = (10, 20, 30, 40, 50)
    print("After removing 30:", remove_from_tuple(t, 30))
