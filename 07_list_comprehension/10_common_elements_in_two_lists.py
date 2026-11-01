"""
Q10: Find common elements between two lists without using set() or intersection().
"""

def find_common(list1, list2):
    return [x for x in list1 if any(x == y for y in list2)]

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    b = [4, 5, 6, 7, 8, 9]
    print("Common elements:", find_common(a, b))
