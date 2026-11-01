"""
Q5: Reverse a tuple without [::-1] or reversed().
"""

def reverse_tuple(tup):
    rev_list = []
    for x in tup:
        rev_list = [x] + rev_list
    return tuple(rev_list)

if __name__ == "__main__":
    t = (1, 2, 3, 4, 5)
    print("Reversed tuple:", reverse_tuple(t))
