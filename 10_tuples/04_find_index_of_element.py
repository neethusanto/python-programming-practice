"""
Q4: Find first index of an element in a tuple without using tuple.index().
"""

def find_tuple_index(tup, target):
    idx = 0
    for x in tup:
        if x == target:
            return idx
        idx += 1
    return -1

if __name__ == "__main__":
    t = ("python", "java", "c++", "rust")
    print("Index of 'c++':", find_tuple_index(t, "c++"))
    print("Index of 'ruby':", find_tuple_index(t, "ruby"))
