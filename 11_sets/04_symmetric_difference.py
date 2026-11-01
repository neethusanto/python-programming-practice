"""
Q4: Find symmetric difference (elements in either set, but not in both) without ^ or symmetric_difference().
"""

def custom_symmetric_difference(set1, set2):
    result = set()
    for x in set1:
        if x not in set2:
            result.add(x)
    for y in set2:
        if y not in set1:
            result.add(y)
    return result

if __name__ == "__main__":
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    print("Symmetric Difference:", custom_symmetric_difference(s1, s2))
