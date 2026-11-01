"""
Q11: Compute Cartesian product of two lists (tuples of all combinations) using list comprehension.
"""

def cartesian_product(list1, list2):
    return [(x, y) for x in list1 for y in list2]

if __name__ == "__main__":
    colors = ["red", "blue"]
    sizes = ["S", "M", "L"]
    print("Cartesian product:", cartesian_product(colors, sizes))
