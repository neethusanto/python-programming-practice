"""
Q6: Check if set A is a superset of set B without issuperset() or >= operator.
"""

def is_superset(set_a, set_b):
    for y in set_b:
        if y not in set_a:
            return False
    return True

if __name__ == "__main__":
    print("{1, 2, 3, 4} superset of {2, 3}:", is_superset({1, 2, 3, 4}, {2, 3}))
    print("{1, 2} superset of {1, 2, 5}:", is_superset({1, 2}, {1, 2, 5}))
