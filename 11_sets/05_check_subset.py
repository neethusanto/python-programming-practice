"""
Q5: Check if set A is a subset of set B without issubset() or <= operator.
"""

def is_subset(set_a, set_b):
    for x in set_a:
        if x not in set_b:
            return False
    return True

if __name__ == "__main__":
    print("{1, 2} subset of {1, 2, 3}:", is_subset({1, 2}, {1, 2, 3}))
    print("{1, 4} subset of {1, 2, 3}:", is_subset({1, 4}, {1, 2, 3}))
