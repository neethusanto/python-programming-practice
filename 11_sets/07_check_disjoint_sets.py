"""
Q7: Check if two sets are disjoint (share no elements) without isdisjoint().
"""

def are_disjoint(set1, set2):
    for x in set1:
        if x in set2:
            return False
    return True

if __name__ == "__main__":
    print("{1, 2} and {3, 4} disjoint:", are_disjoint({1, 2}, {3, 4}))
    print("{1, 2} and {2, 3} disjoint:", are_disjoint({1, 2}, {2, 3}))
