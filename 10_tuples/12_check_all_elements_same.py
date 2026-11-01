"""
Q12: Check if all elements in a tuple are identical without set().
"""

def all_identical(tup):
    if not tup:
        return True
    first = tup[0]
    for x in tup:
        if x != first:
            return False
    return True

if __name__ == "__main__":
    print("(5, 5, 5, 5) all identical:", all_identical((5, 5, 5, 5)))
    print("(5, 5, 3, 5) all identical:", all_identical((5, 5, 3, 5)))
