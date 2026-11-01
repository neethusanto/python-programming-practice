"""
Q10: Find intersection (common elements) of two lists without using set() or intersection().
"""

def list_intersection(l1, l2):
    common = []
    for x in l1:
        if any(x == y for y in l2):
            # Check unique in common
            if not any(x == c for c in common):
                common.append(x)
    return common

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 2]
    b = [2, 4, 6, 8, 4]
    print("Intersection:", list_intersection(a, b))
