"""
Q11: Slice a tuple between start and end indices without tuple slicing syntax.
"""

def slice_tuple(tup, start, end):
    sliced = []
    idx = 0
    for x in tup:
        if idx >= start and idx < end:
            sliced.append(x)
        idx += 1
    return tuple(sliced)

if __name__ == "__main__":
    t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print("Slice (2 to 6):", slice_tuple(t, 2, 6))
