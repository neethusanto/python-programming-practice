"""
Q8: Concatenate/merge two tuples into one without using the + operator.
"""

def merge_tuples(t1, t2):
    items = []
    for x in t1:
        items.append(x)
    for y in t2:
        items.append(y)
    return tuple(items)

if __name__ == "__main__":
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    print("Merged:", merge_tuples(t1, t2))
