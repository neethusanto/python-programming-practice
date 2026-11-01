"""
Q6: Check whether an item exists in a tuple without using the 'in' operator.
"""

def element_in_tuple(tup, target):
    for x in tup:
        if x == target:
            return True
    return False

if __name__ == "__main__":
    t = (10, 20, 30, 40)
    print("30 in tuple:", element_in_tuple(t, 30))
    print("50 in tuple:", element_in_tuple(t, 50))
