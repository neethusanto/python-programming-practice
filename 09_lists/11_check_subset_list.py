"""
Q11: Check if list A is a subset of list B without using set.issubset().
"""

def is_subset(sub, main):
    for x in sub:
        found = False
        for y in main:
            if x == y:
                found = True
                break
        if not found:
            return False
    return True

if __name__ == "__main__":
    print("[1, 3] in [1, 2, 3, 4]:", is_subset([1, 3], [1, 2, 3, 4]))
    print("[1, 5] in [1, 2, 3, 4]:", is_subset([1, 5], [1, 2, 3, 4]))
