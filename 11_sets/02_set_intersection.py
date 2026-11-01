"""
Q2: Find intersection of two sets without intersection() method or & operator.
"""

def custom_intersection(set1, set2):
    result = set()
    for x in set1:
        if x in set2:
            result.add(x)
    return result

if __name__ == "__main__":
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}
    print("Intersection:", custom_intersection(s1, s2))
