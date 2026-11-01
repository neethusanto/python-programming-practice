"""
Q1: Find the number of elements in a tuple without using len().
"""

def tuple_length(tup):
    count = 0
    for _ in tup:
        count += 1
    return count

if __name__ == "__main__":
    t = (10, "apple", 3.14, True, [1, 2])
    print("Tuple length:", tuple_length(t))
