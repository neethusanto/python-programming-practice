"""
Q1: Find union of two sets without using the built-in union() method or | operator.
"""

def custom_union(set1, set2):
    result = set()
    for x in set1:
        result.add(x)
    for y in set2:
        result.add(y)
    return result

if __name__ == "__main__":
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    print("Union:", custom_union(s1, s2))
