"""
Q14: Compute Cartesian product of two sets as a set of tuples.
"""

def cartesian_product_sets(s1, s2):
    product = set()
    for x in s1:
        for y in s2:
            product.add((x, y))
    return product

if __name__ == "__main__":
    a = {1, 2}
    b = {'a', 'b'}
    print("Cartesian product:", cartesian_product_sets(a, b))
