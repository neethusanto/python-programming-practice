"""
Q3: Find set difference (A - B) without using difference() method or - operator.
"""

def custom_difference(set1, set2):
    result = set()
    for x in set1:
        if x not in set2:
            result.add(x)
    return result

if __name__ == "__main__":
    s1 = {1, 2, 3, 4, 5}
    s2 = {2, 4, 6}
    print("Difference (s1 - s2):", custom_difference(s1, s2))
