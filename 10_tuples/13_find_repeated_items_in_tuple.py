"""
Q13: Find all repeated/duplicate items in a tuple without Counter or set().
"""

def find_duplicates(tup):
    duplicates = []
    seen = []
    for x in tup:
        already_seen = False
        for s in seen:
            if s == x:
                already_seen = True
                break
        if already_seen:
            in_dup = False
            for d in duplicates:
                if d == x:
                    in_dup = True
                    break
            if not in_dup:
                duplicates.append(x)
        else:
            seen.append(x)
    return tuple(duplicates)

if __name__ == "__main__":
    t = (1, 2, 3, 2, 4, 5, 1, 6, 2)
    print("Duplicates:", find_duplicates(t))
